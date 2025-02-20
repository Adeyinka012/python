function showTime(){
    var Date = new Date();
    var h = date.getHours();
    var n = date.getMinutes();
    var s = date.getSeconds();
    var session = "AM"

    if(h==0){
        h = 12
    }
    if(h >12){
        h=h-12;
        session = "PM"
    }
    h = (h<10)? "0" + h:h
    m = (n<10)? "0" + n:n
    s = (s<10)? "0" + s:s
    var time = h + ":" + m +":" + s +" " + session

    document.getElementById("myClockDisplay").innerText =time
    setTimeout(showTime,1000 )
}
showTime()