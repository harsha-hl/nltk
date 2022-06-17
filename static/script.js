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
    position(200,250,90,"static/beaker_empty.png");
    position(800,350,45,"static/beaker_empty.png");

});
