var i = 0;
var max_time = 60; //secs
var tick_time = 15 //Time in seconds left to start the ticking sound
function timedCount() {
    i = i + 1;
    postMessage(max_time - i);
    if(i < tick_time +1){
 

    }
    setTimeout("timedCount()",1000);
}

timedCount(); 
