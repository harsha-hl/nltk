//flask run -h localhost -p 3000
//var counter=0;
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


document.addEventListener("DOMContentLoaded", myfunction);
//function myfunction(type)
function myfunction()
{   
    

    var objs = document.getElementById('myData').value;
    console.log(objs);
    console.log(objs.length);

    objs = objs.slice(1, objs.length-1);
    console.log("typeof"+typeof(objs));    //output is string
    var o = [];
    console.log("helloo"+objs);
    //for(var p=0;p<objs.length;p++)
    //{
    while (objs.length > 0)
    {
        o.push(objs.slice(1,objs.indexOf(']')  - 1));
        objs = objs.slice(objs.indexOf(']') + 3);
        console.log("ananyaaaaaaaa"+objs);
        console.log("indexxx"+objs.indexOf(']'));
    }
    happy = [];
    sentence = [];
    console.log("the new isssss"+o);
    console.log("length of o issss"+o.length);
    
    for(var b=0;b<o.length;b++)
    {
        //froommmm
        console.log("jkjkjkjkjkj"+o[b]);
        while(o[b].length>0)
        {
        sentence.push( JSON.parse(o[b].slice(1,o[b].indexOf('}') +1)));
        console.log("typeee"+typeof(sentence[0]));
       
        o[b] = o[b].slice(o[b].indexOf('}') +4);
        }
     //   console.log("sentence of b  dot src isss"+sentence[0].name);
       // console.log("sentence of b of newww"+ sentence[1].name);
       console.log("sentenceddddd isss" + sentence);
       console.log("sentence of 0 isss" + sentence[0]);
       console.log("len of sentence"+ sentence.length);
       console.log("sentence individ"+sentence[0].name);
        //toooooo
      //  function next1()
     //   {
        next.apply(this,sentence);
     //   }
//here
        sentence = [];
        
    }
}
 // 

function next()
{
    //console.log("ddaaddaa"+sentence[0].name);
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
           // for(var p=0;p<sentence.length;p++)
            //{ 
      
             //  if(p%2===0 && p!==0)
              // {
                //    x+=300;
              // }
             //  console.log("sentence[p].pos"+sentence[p].position);
               let result_up = (sentence[p].position).localeCompare("up");   //o[b][p]  or o[b[p]]
               let result_down = (sentence[p].position).localeCompare("down");
               let result_inside = (sentence[p].position).localeCompare("in");   //into
               let result_pour = (sentence[p].verb).localeCompare("pour");
               if(result_up === 0)
                {
                    console.log(" heyyy i am in up sentence[p].src"+sentence[p].src);
                  var t = y+150;
                 position(x,t,z,sentence[p].src);
                  

                // var img = document.getElementById('imageid'); 
                 //or however you get a handle to the IMG
                
                

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
               

        
          //  }
    }
    x+=300;
   
}
/*

switch (type.className){
    //  counter++;
      case "next": next(); break;
      
   }
*/
