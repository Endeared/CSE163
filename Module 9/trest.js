cookieBtn = document.getElementById("bigCookie");

setInterval(function(){
    Game.lastClick -= 1000;
    cookieBtn.click();
}, 1);