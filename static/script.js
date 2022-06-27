//flask run -h localhost -p 3000
//var counter=0;

function position(x,y,deg,path){
    const space = document.getElementById("space");
    const img1 = document.createElement('img');
    img1.src = path;
    img1.style.width = "200px";
    img1.style.height = "250px";
    img1.style.position = "absolute";
    img1.style.left = x + "px";
    img1.style.top = y + "px";
    img1.style.transform = "rotate(" + deg + "deg)";
    space.appendChild(img1);
}


document.addEventListener("DOMContentLoaded", myfunction);
function myfunction(type)
{   
    

    var objs = document.getElementById('myData').value;
    objs = objs.slice(1, objs.length-1);
    var o = [];
    while (objs.length > 0){
        o.push(JSON.parse(objs.slice(1,objs.indexOf('}') + 1)));
        objs = objs.slice(objs.indexOf('}') + 4);
    }
    console.log(o);
    console.log(o.length);
    
   

function next()
{
    console.log(o[3].name);
  //  position(400,400,z,o[3].src);




  var x=100;
  var y=550;
  var z=00;
      for(var p=0;p<o.length;p++)
      {
         if(p%2===0 && p!==0)
         {
              x+=300;
         }
         let result_up = (o[p].pos).localeCompare("up");
         let result_down = (o[p].pos).localeCompare("down");
         let result_inside = (o[p].pos).localeCompare("inside");
         let result_pour = (o[p].verb).localeCompare("pour");
         if(result_up === 0)
          {
              //y-=110;
              var k = y-150;
              position(x,k,z,o[p].src);
              console.log("y = 440"+y);
              
          }
          if(result_down === 0)
          {
              var f = y+110;
              position(x,f,z,o[p].src);
          }
          if(result_inside === 0)
          {
              position(x,(y-50),z,o[p].src);
          }
          if(result_pour === 0)
          {
              var angle = z+ 225;
             // var height = y -250 ;
              position((x+70),(y-250),angle,o[p].src);
            // position(x,height,z,o[p].src);
          }
          if(result_up !== 0 && result_down !==0 && result_pour !== 0 && result_inside!==0)
          {
              
              position(x,y,z,o[p].src);
          }
  
      }

}

switch (type.className){
  //  counter++;
    case "next": next(); break;
    
 }
 

}




