'use strict';

class Color {
  constructor(r, g, b) {
    this.set(r, g, b);
  }
  
  toString() {
    return `rgb(${Math.round(this.r)}, ${Math.round(this.g)}, ${Math.round(this.b)})`;
  }

  set(r, g, b) {
    this.r = this.clamp(r);
    this.g = this.clamp(g);
    this.b = this.clamp(b);
  }

  hueRotate(angle = 0) {
    angle = angle / 180 * Math.PI;
    const sin = Math.sin(angle);
    const cos = Math.cos(angle);

    this.multiply([
      0.213 + cos * 0.787 - sin * 0.213,
      0.715 - cos * 0.715 - sin * 0.715,
      0.072 - cos * 0.072 + sin * 0.928,
      0.213 - cos * 0.213 + sin * 0.143,
      0.715 + cos * 0.285 + sin * 0.140,
      0.072 - cos * 0.072 - sin * 0.283,
      0.213 - cos * 0.213 - sin * 0.787,
      0.715 - cos * 0.715 + sin * 0.715,
      0.072 + cos * 0.928 + sin * 0.072,
    ]);
  }

  grayscale(value = 1) {
    this.multiply([
      0.2126 + 0.7874 * (1 - value),
      0.7152 - 0.7152 * (1 - value),
      0.0722 - 0.0722 * (1 - value),
      0.2126 - 0.2126 * (1 - value),
      0.7152 + 0.2848 * (1 - value),
      0.0722 - 0.0722 * (1 - value),
      0.2126 - 0.2126 * (1 - value),
      0.7152 - 0.7152 * (1 - value),
      0.0722 + 0.9278 * (1 - value),
    ]);
  }

  sepia(value = 1) {
    this.multiply([
      0.393 + 0.607 * (1 - value),
      0.769 - 0.769 * (1 - value),
      0.189 - 0.189 * (1 - value),
      0.349 - 0.349 * (1 - value),
      0.686 + 0.314 * (1 - value),
      0.168 - 0.168 * (1 - value),
      0.272 - 0.272 * (1 - value),
      0.534 - 0.534 * (1 - value),
      0.131 + 0.869 * (1 - value),
    ]);
  }

  saturate(value = 1) {
    this.multiply([
      0.213 + 0.787 * value,
      0.715 - 0.715 * value,
      0.072 - 0.072 * value,
      0.213 - 0.213 * value,
      0.715 + 0.285 * value,
      0.072 - 0.072 * value,
      0.213 - 0.213 * value,
      0.715 - 0.715 * value,
      0.072 + 0.928 * value,
    ]);
  }

  multiply(matrix) {
    const newR = this.clamp(this.r * matrix[0] + this.g * matrix[1] + this.b * matrix[2]);
    const newG = this.clamp(this.r * matrix[3] + this.g * matrix[4] + this.b * matrix[5]);
    const newB = this.clamp(this.r * matrix[6] + this.g * matrix[7] + this.b * matrix[8]);
    this.r = newR;
    this.g = newG;
    this.b = newB;
  }

  brightness(value = 1) {
    this.linear(value);
  }
  contrast(value = 1) {
    this.linear(value, -(0.5 * value) + 0.5);
  }

  linear(slope = 1, intercept = 0) {
    this.r = this.clamp(this.r * slope + intercept * 255);
    this.g = this.clamp(this.g * slope + intercept * 255);
    this.b = this.clamp(this.b * slope + intercept * 255);
  }

  invert(value = 1) {
    this.r = this.clamp((value + this.r / 255 * (1 - 2 * value)) * 255);
    this.g = this.clamp((value + this.g / 255 * (1 - 2 * value)) * 255);
    this.b = this.clamp((value + this.b / 255 * (1 - 2 * value)) * 255);
  }

  hsl() {
    const r = this.r / 255;
    const g = this.g / 255;
    const b = this.b / 255;
    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
      h = s = 0;
    } else {
      const d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      switch (max) {
        case r:
          h = (g - b) / d + (g < b ? 6 : 0);
          break;

        case g:
          h = (b - r) / d + 2;
          break;

        case b:
          h = (r - g) / d + 4;
          break;
      }
      h /= 6;
    }

    return {
      h: h * 100,
      s: s * 100,
      l: l * 100,
    };
  }

  clamp(value) {
    if (value > 255) {
      value = 255;
    } else if (value < 0) {
      value = 0;
    }
    return value;
  }
}

class Solver {
  constructor(target, baseColor) {
    this.target = target;
    this.targetHSL = target.hsl();
    this.reusedColor = new Color(0, 0, 0);
  }

  solve() {
    const result = this.solveNarrow(this.solveWide());
    return {
      values: result.values,
      loss: result.loss,
      filter: this.css(result.values),
    };
  }

  solveWide() {
    const A = 5;
    const c = 15;
    const a = [60, 180, 18000, 600, 1.2, 1.2];

    let best = { loss: Infinity };
    for (let i = 0; best.loss > 25 && i < 3; i++) {
      const initial = [50, 20, 3750, 50, 100, 100];
      const result = this.spsa(A, a, c, initial, 1000);
      if (result.loss < best.loss) {
        best = result;
      }
    }
    return best;
  }

  solveNarrow(wide) {
    const A = wide.loss;
    const c = 2;
    const A1 = A + 1;
    const a = [0.25 * A1, 0.25 * A1, A1, 0.25 * A1, 0.2 * A1, 0.2 * A1];
    return this.spsa(A, a, c, wide.values, 500);
  }

  spsa(A, a, c, values, iters) {
    const alpha = 1;
    const gamma = 0.16666666666666666;

    let best = null;
    let bestLoss = Infinity;
    const deltas = new Array(6);
    const highArgs = new Array(6);
    const lowArgs = new Array(6);

    for (let k = 0; k < iters; k++) {
      const ck = c / Math.pow(k + 1, gamma);
      for (let i = 0; i < 6; i++) {
        deltas[i] = Math.random() > 0.5 ? 1 : -1;
        highArgs[i] = values[i] + ck * deltas[i];
        lowArgs[i] = values[i] - ck * deltas[i];
      }

      const lossDiff = this.loss(highArgs) - this.loss(lowArgs);
      for (let i = 0; i < 6; i++) {
        const g = lossDiff / (2 * ck) * deltas[i];
        const ak = a[i] / Math.pow(A + k + 1, alpha);
        values[i] = fix(values[i] - ak * g, i);
      }

      const loss = this.loss(values);
      if (loss < bestLoss) {
        best = values.slice(0);
        bestLoss = loss;
      }
    }
    return { values: best, loss: bestLoss };

    function fix(value, idx) {
      let max = 100;
      if (idx === 2 /* saturate */) {
        max = 7500;
      } else if (idx === 4 /* brightness */ || idx === 5 /* contrast */) {
        max = 200;
      }

      if (idx === 3 /* hue-rotate */) {
        if (value > max) {
          value %= max;
        } else if (value < 0) {
          value = max + value % max;
        }
      } else if (value < 0) {
        value = 0;
      } else if (value > max) {
        value = max;
      }
      return value;
    }
  }

  loss(filters) {
    // Argument is array of percentages.
    const color = this.reusedColor;
    color.set(0, 0, 0);

    color.invert(filters[0] / 100);
    color.sepia(filters[1] / 100);
    color.saturate(filters[2] / 100);
    color.hueRotate(filters[3] * 3.6);
    color.brightness(filters[4] / 100);
    color.contrast(filters[5] / 100);

    const colorHSL = color.hsl();
    return (
      Math.abs(color.r - this.target.r) +
      Math.abs(color.g - this.target.g) +
      Math.abs(color.b - this.target.b) +
      Math.abs(colorHSL.h - this.targetHSL.h) +
      Math.abs(colorHSL.s - this.targetHSL.s) +
      Math.abs(colorHSL.l - this.targetHSL.l)
    );
  }

  css(filters) {
    function fmt(idx, multiplier = 1) {
      return Math.round(filters[idx] * multiplier);
    }
    return `invert(${fmt(0)}%) sepia(${fmt(1)}%) saturate(${fmt(2)}%) hue-rotate(${fmt(3, 3.6)}deg) brightness(${fmt(4)}%) contrast(${fmt(5)}%)`;
  }
}

function hexToRgb(hex) {
  // Expand shorthand form (e.g. "03F") to full form (e.g. "0033FF")
  const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
  hex = hex.replace(shorthandRegex, (m, r, g, b) => {
    return r + r + g + g + b + b;
  });

  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result
    ? [
      parseInt(result[1], 16),
      parseInt(result[2], 16),
      parseInt(result[3], 16),
    ]
    : null;
}

function hexToFilter(hex){
  //console.log("Hereee in function hex to filter")
  const rgb = hexToRgb(hex);
  const color = new Color(rgb[0], rgb[1], rgb[2]);
  const solver = new Solver(color);
  const result = solver.solve();
  return result.filter;
}

//flask run -h localhost -p 3000
//var counter=0;
var sentence_index = 0, numOfSentences, sentences=[], o, paragraph, toDisplaySentences;
//let x= 100;
function position(x,y,deg,path,hex_image){
    const space = document.getElementById("space");
    const img1 = document.createElement('img');
    img1.src = path;
    // img1.style.width = "200px";
  //  img1.style.height = "200px";
   //img1.style.height = "auto";
   var width_ppt = (path).localeCompare("static/pptTestTube.png");
   if(width_ppt===0)
   {
    console.log("i am in the width loop");
    img1.style.width = "50px";
    img1.style.height = "20px";
   }
   else
   {
    console.log("i am in the else loop");
    img1.style.height = "200px";
    img1.style.width = "auto";
   }
  
  // img1.style.width = "auto";
    img1.style.position = "absolute";
    img1.style.left = x + "px";
    img1.style.filter = hexToFilter(hex_image);
    img1.style.bottom = y+"px";
    img1.style.transform = "rotate(" + deg + "deg)";
    space.appendChild(img1);
}

function prevSentence(){
  if(sentence_index > 0){
    sentence_index --;
    decodeSentence();
  }
}

function nextSentence(){
  if(sentence_index < numOfSentences-1){
    sentence_index ++;
    decodeSentence();
  }
}

document.addEventListener("DOMContentLoaded", function (){

$('.iii').attr('style', hexToFilter("#ffa000"));
    $('.image2').attr('style', hexToFilter("#00ff00"));
    var objs = document.getElementById('myData').value;
    const para = document.getElementById('para').value;
    toDisplaySentences = para.match( /[^\.!\?]+[\.!\?]+/g );



    console.log(objs);
    console.log(objs.length);
  
    objs = objs.slice(1, objs.length-1);
    o = [];
    while (objs.length > 0)
    {
        o.push(objs.slice(1,objs.indexOf(']')  - 1));
        objs = objs.slice(objs.indexOf(']') + 3);
    }
    numOfSentences = o.length;
    for(let i=0;i<numOfSentences;i++){
      let senten = [];
      while(o[i].length>0)
        {
        senten.push( JSON.parse(o[i].slice(1,o[i].indexOf('}') +1)));
  
        console.log("typeee"+typeof(senten[0]));
       
        o[i] = o[i].slice(o[i].indexOf('}') +4);
        }
        sentences.push(senten);
    }
    console.log(sentences);
    decodeSentence();
  

  });

function decodeSentence()
{
    let images = Array.prototype.slice.call(document.getElementById("space").getElementsByTagName("img"));
    for(let i=0;i<images.length;i++)
      images[i].remove();
    document.getElementById("statement").innerHTML = toDisplaySentences[sentence_index];
    let sentence = sentences[sentence_index];
    console.log("DEBUGGGgGGGGGGGGG");
    console.log(sentence);
    console.log(typeof(sentence[0]));
    console.log("DEBUGGGgGGGGGGGGG");

    var k = sentence.length;                     //sentence has the objects in one sentence
    console.log("len of sentence in next"+k);



    if(sentence.length===0)
    {
      console.log("SNETENCE_INDEXXXXXXX"+sentence_index);
      let no_object = sentence_index;
      no_object--;
       if(no_object.length===0)
       {
        while(no_object!==0)
        {
        no_object--;
        }
       }
       let images1 = Array.prototype.slice.call(document.getElementById("space").getElementsByTagName("img"));
       for(let i=0;i<images1.length;i++)
          images1[i].remove();
        let sents = sentences[no_object];
        var le=sents.length;
       
        for(var t=0;t<le;t++)
        {
            console.log("i am in the new pos"+sents[t].name);
          var z=0;
          var x_new=sents[t].positionx;
          var y_new=sents[t].positiony;


          var hex_image_new=sents[t].colour;
                  console.log("This is hex of image"+hex_image_new);
                  position(x_new,y_new,z,sents[t].src,hex_image_new);
        }
    }
     else
     {

    for(var p = 0;p<k;p++)       //p is the number of objects in a sentence
    {
        console.log("inside sentence loop"+ sentence[p].name);
        console.log("sentence[p].pos bbbbbbb\n\n"+sentence[p].positionx);
        var x=sentence[p].positionx;
       
        var y = sentence[p].positiony;
        var z=0;
              console.log("just here");  
                    console.log(" heyyy i am in up sentence[p].src"+sentence[p].src);
                  console.log(" heyyy i am in  sentence[p].src"+sentence[p].src);
                  var hex_image=sentence[p].colour;
                  console.log("This is hex of image"+hex_image);
                  position(x,y,z,sentence[p].src,hex_image);
              
    }
  
}
}

