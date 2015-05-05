var i = 0;
var max_time = 60; //secs
function timedCount() {
    i = i + 1;
    postMessage(max_time - i);
    setTimeout("timedCount()",1000);
}

timedCount(); 
