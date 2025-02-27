var dice;
// dice image from value 1 to 6 are given in an array, codes are from Die face Emoji Emojipedia
var dices = ['&#9856;', '&#9857;', '&#9858;', '&#9859;', '&#9860;', '&#9861;' ];
var stopped = true;
var t;

function change(){
    var random = Math.floor(Math.random() * 6)
    dice.innerHTML = dices[random]
}

function stopstart(){
    if(stopped){
        stopped = false;
        t=setInterval(change,100);
    }
    else{
        clearInterval(t)
        stopped = true
    }
}

// calling function

window.onload = function(){
    dice = document.getElementById("dice");
    stopstart()
}