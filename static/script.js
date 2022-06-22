function position(x,y,deg,path){
    const space = document.getElementById("space");
    const img1 = document.createElement('img');
    img1.src = path;
    img1.style.width = "200px";
    img1.style.position = "absolute";
    img1.style.left = x + "px";
    img1.style.top = y + "px";
    img1.style.transform = "rotate(" + deg + "deg)";
    space.appendChild(img1);
}

document.addEventListener("DOMContentLoaded", function(){
    var objs = document.getElementById('myData').value;
    objs = objs.slice(1, objs.length-1);
    var o = [];
    while (objs.length > 0){
        o.push(JSON.parse(objs.slice(1,objs.indexOf('}') + 1)));
        objs = objs.slice(objs.indexOf('}') + 4);
    }
    console.log(o);

    // console.log(typeof(JSON.parse(objs[0])));
    position(200,250,00,"static/beaker_empty.png");
    position(500,250,45,"static/beaker_empty.png");
    position(900,250,90,"static/beaker_empty.png");


});
