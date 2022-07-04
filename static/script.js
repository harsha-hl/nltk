//flask run -h localhost -p 3000
//var counter=0;
var sentence_index = 0, numOfSentences, sentences=[], o, paragraph, toDisplaySentences;
//let x= 100;
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



    if(sentence.length===0)
    {
      console.log("SNETENCE_INDEXXXXXXX"+sentence_index);
     // if(sentence_index > 0){
      //  sentence_index --;
      let no_object = sentence_index;
      no_object--;
       // decodeSentence();
       if(no_object.length===0)
       {
        while(no_object!==0)
        {
        no_object--;
        }
       }
       let images1 = Array.prototype.slice.call(document.getElementById("space").getElementsByTagName("img"));
       for(i=0;i<images1.length;i++)
          images1[i].remove();
        let sents = sentences[no_object];
        var le=sents.length;
       
        for(var t=0;t<le;t++)
        {
          let result_pournew = (sents[t].verb).localeCompare("pour");
          if (result_pournew ===0)
          {
            console.log("i am in the new pour"+sents[t].name);
            var znew=-125;
            var x_newnew=420;
            var y_newnew=-400;
            position(x_newnew,y_newnew,znew,sents[t].src); 
          }
          else{
            console.log("i am in the new pos"+sents[t].name);
          var z=00;
          var x_new=sents[t].positionx;
          var y_new=sents[t].positiony;
          position(x_new,y_new,z,sents[t].src);
          }
        }
     // }
    }
     else
     {

    for(var p = 0;p<k;p++)       //p is the number of objects in a sentence
    {
        console.log("inside sentence loop"+ sentence[p].name);
        console.log("sentence[p].pos bbbbbbb\n\n"+sentence[p].positionx);
        var x=sentence[p].positionx;
       
        var y = sentence[p].positiony;
        var z=00;
              console.log("just here");
            
               let result_pour = (sentence[p].verb).localeCompare("pour");
              
                    console.log(" heyyy i am in up sentence[p].src"+sentence[p].src);
                //  var t = y+150;
              //   position(x,y,z,sentence[p].src);
             //   } 
                  
                if(result_pour === 0)
                {
                  console.log(" heyyy i am in pour sentence[p].src"+sentence[p].src);
                  var angle = z - 125;
                 // var new_x = x+70;
                  //var new_y = y+200;
                  var new_x=420;
                  var new_y=-400;
                  console.log("typeof(x)"+typeof(x));
                  console.log("ANGLEEEEEE"+angle);
                  console.log("xxxxxxxxxxxxxxxxxxx"+new_x);
                  console.log("yyyyyyyyyyyyyyyyyyyyy"+new_y);
                  
                  position(new_x,new_y,angle,sentence[p].src);
                }
                else{
                  console.log(" heyyy i am in  sentence[p].src"+sentence[p].src);
                   
                     position(x,y,z,sentence[p].src);
                }
    }
  //  x+=300; 
}
}