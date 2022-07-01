//flask run -h localhost -p 3000
//var counter=0;
var sentence_index = 0, numOfSentences, sentences=[], o, paragraph, toDisplaySentences;
let x= 100;
function position(x,y,deg,path){
    const space = document.getElementById("space");
    const img1 = document.createElement('img');
    img1.src = path;
    img1.style.width = "200px";
    img1.style.height = "auto";
    img1.style.position = "absolute";
    img1.style.left = x + "px";
  //  img1.style.top = y + "px";
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
    for(i=0;i<images.length;i++)
      images[i].remove();
    document.getElementById("statement").innerHTML = toDisplaySentences[sentence_index];
    let sentence = sentences[sentence_index];
    console.log("DEBUGGGgGGGGGGGGG");
    console.log(sentence);
    console.log(typeof(sentence[0]));
    console.log("DEBUGGGgGGGGGGGGG");

    var k = sentence.length;                     //sentence has the objects in one sentence
    console.log("len of sentence in next"+k);
    for(var p = 0;p<k;p++)       //p is the number of objects in a sentence
    {
        console.log("inside sentence loop"+ sentence[p].name);
        console.log("sentence[p].pos"+sentence[p].position);
       // var x=100;
        //var y=350;
        var y = -600;
        var z=00;
              console.log("just here");
               let result_up = (sentence[p].position).localeCompare("up");   //o[b][p]  or o[b[p]]
               let result_down = (sentence[p].position).localeCompare("down");
               let result_inside = (sentence[p].position).localeCompare("in");   //into
               let result_pour = (sentence[p].verb).localeCompare("pour");
               if(result_up === 0)
                {
                    console.log(" heyyy i am in up sentence[p].src"+sentence[p].src);
                  var t = y+150;
                 position(x,t,z,sentence[p].src);
                } 
                  
              if(result_down === 0)
                {
                    console.log(" heyyy i am in down sentence[p].src"+sentence[p].src);
                    var f = y-110;
                    position(x,f,z,sentence[p].src);
                }
                if(result_inside === 0)
                {
                    console.log(" heyyy i am in inside sentence[p].src"+sentence[p].src);
                    position(x,(y+50),z,sentence[p].src);
                }
                if(result_pour === 0)
                {
                    console.log(" heyyy i am in pour sentence[p].src"+sentence[p].src);
                    var angle = z+ 225;
                   // var height = y -250 ;
                    position((x+70),(y+200),angle,sentence[p].src);
                  // position(x,height,z,o[p].src);
                }
                if(result_up !== 0 && result_down !==0 && result_pour !== 0 && result_inside!==0)
                {
                    console.log(" heyyy i am in default sentence[p].src"+sentence[p].src);
                    position(x,y,z,sentence[p].src);
                }
    }
  //  x+=300; 
}