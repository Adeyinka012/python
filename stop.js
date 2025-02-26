// window.onload = function {} {
// }
window.onload=function(){
    var seconds =0;
    var milliseconds = 0;
    var appendmilliseconds =document.getElementById('milliseconds')
    var appendsecod =document.getElementById('seconds')
    var buttonStart =document.getElementById('buttonStart')
    var buttonStop =document.getElementById('buttonStop')
    var buttonReset =document.getElementById('buttonReset')
    var Interval;
    buttonStart.onclick= function(){
        clearInterval(Interval)
        Interval= setInterval(StartTimer, 10)
    }

    
}