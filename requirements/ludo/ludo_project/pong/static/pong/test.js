/***************************************** Setup *****************************************/

let gameArea = document.getElementById("test-target"),
htmlme = document.getElementById("me"),
htmladversary = document.getElementById("adversary"),
htmlBall = document.getElementsByClassName("ball")[0];

const ballStyle = getComputedStyle(htmlBall);
const meStyle = getComputedStyle(htmlme);
const adversaryStyle = getComputedStyle(htmladversary);

const screenHeight = window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
htmladversary.style.left = screenWidth - parseInt(meStyle.width, 10) - 10 + 'px';


/***************************************** Classes *****************************************/

class Player {
    constructor(name) {
        this.name = name;
        this.points = 0;
        this.pos = screenHeight / 2;
        this.up = false;
        this.down = false;
    }
    move(playerStyle) {
        let mvt = this.down - this.up;
        const newPos = this.pos + mvt * screenHeight / 300;
        if (newPos + parseInt(playerStyle.height, 10) / 2 < screenHeight && newPos > parseInt(playerStyle.height, 10) / 2) {
            this.pos = newPos;
        }
    }
}

class Ball {
    constructor() {
        this.pos = {x: screenWidth / 2, y: screenHeight / 2};
        this.speed = screenHeight / 500;
        this.angle = Math.PI;
        this.size = screenHeight / 100;
    }
    move() {
        this.pos['x'] += this.speed * Math.cos(this.angle);
        this.pos['y'] -= this.speed * Math.sin(this.angle);
    }
    init() {
        this.pos = {x: screenWidth / 2, y: screenHeight / 2};
        this.speed = screenHeight / 500;
        this.angle = Math.PI;
        this.size = screenHeight / 100;
    }
}

/***************************************** Players movements *****************************************/

let me = new Player("me");
let adversary = new Player("adversary");

// Events for keyboard inputs
gameArea.addEventListener("keydown", (e) => { // Booleans with on press and on release (anyway will be a websocket) !!
    if (e.repeat) {
        return;
    }
    if (`${e.key}` === 'w') {
        me.up = true;
    } else if (`${e.key}` === 's') {
        me.down = true;
    }
});

gameArea.addEventListener("keyup", (e) => { // Booleans with on press and on release (anyway will be a websocket) !!    
    if (`${e.key}` === 'w') {
        me.up = false;
    } else if (`${e.key}` === 's') {
        me.down = false;
    }
});

/***************************************** Websockets *****************************************/

console.log("ws://" + window.location.host + '/pong/ws/me/')
const exampleSocket = new WebSocket('ws://localhost:8005/pong/'); // Probably add room name

exampleSocket.onopen = function(event) {
    sendStartGameData("gameStart", screenHeight, screenWidth, parseInt(meStyle.height, 10)); // Player names maybe ?
    console.log("Socket opened in the front");
};

exampleSocket.onclose = function() {
    console.log("Socket closed in the front");
}

exampleSocket.onerror = function(event) {
    console.log("Socket error");
}

exampleSocket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    
    me.pos = data.mePos;
    adversary.pos = data.adversaryPos
};

function sendStartGameData(type, screenHeight, screenWidth, playerHeight) {
    // Construct a msg object containing the data the server needs to process the message from the chat client.
    const gameData = {
      type: type,
      playerHeight: playerHeight,
      screenHeight: screenHeight,
      screenWidth: screenWidth,
    };
  
    // Send the msg object as a JSON-formatted string.
    exampleSocket.send(JSON.stringify(gameData));
}

function sendData(type, meUp, meDown) {
    // Construct a msg object containing the data the server needs to process the message from the chat client.
    const gameData = {
      type: type,
      meUp: meUp,
      meDown: meDown,
    };
  
    // Send the msg object as a JSON-formatted string.
    exampleSocket.send(JSON.stringify(gameData));
}

/***************************************** Game logic *****************************************/

function isPlayerCollision(ball, player, playerStyle) {
    if (ball.pos['y'] > player.pos - (parseInt(playerStyle.height, 10) / 2) && 
        ball.pos['y'] < player.pos + (parseInt(playerStyle.height, 10) / 2)) {
        return true;
    }
    return false;
}

function playerCollision(ball, player, playerStyle) {
    let impactToMid = (ball.pos['y'] - player.pos) / (parseInt(playerStyle.height, 10) * 0.5); // > 0 quand la balle tape en DESSOUS du milieu
    if (player.name === "me") {
        ball.angle = - (Math.PI / 4) * impactToMid;
    } else if (player.name === "adversary") {
        ball.angle = Math.PI + (Math.PI / 4) * impactToMid;
    }
}

function normAngle(angle) {
    if (angle > Math.PI) {
        angle -= 2 * Math.PI;
    } else if (angle < - Math.PI) {
        angle += 2 * Math.PI;
    }
    // return angle;
}

let ball = new Ball();

function gameLoop() {
    // End of point
    if (ball.pos['x'] > screenWidth) {
        me.points++;
        ball.init();
    } else if (ball.pos['x'] < 0) {
        adversary.points++;
        ball.init();
    }
    document.getElementById("score1").innerHTML = me.points.toString();
    document.getElementById("score2").innerHTML = adversary.points.toString();

    // Update positions
    ball.move();
    // me.move(meStyle);
    sendData("gameState", me.up, me.down);
    console.log("Data sent to back");

    // Update front
    htmlBall.style.top = ball.pos['y'] - parseInt(ballStyle.height, 10) / 2 + 'px';
    htmlBall.style.left = ball.pos['x'] - parseInt(ballStyle.width, 10) / 2 + 'px';
    htmlme.style.top = me.pos - parseInt(meStyle.height, 10) / 2 + 'px';
    htmladversary.style.top = adversary.pos - parseInt(adversaryStyle.height, 10) / 2 + 'px';

    // Collision with adversary
    if (ball.pos['x'] >= screenWidth - (parseInt(ballStyle.width, 10) + parseInt(adversaryStyle.width, 10)) && isPlayerCollision(ball, adversary, adversaryStyle)) {
        playerCollision(ball, adversary, adversaryStyle);
    }

    // Collision with me
    if (ball.pos['x'] <= parseInt(ballStyle.width, 10) + parseInt(meStyle.width, 10) && isPlayerCollision(ball, me, meStyle)) {
        playerCollision(ball, me, meStyle);
    }

    // Collision with walls
    if (ball.pos['y'] <= parseInt(ballStyle.height, 10) / 2 || ball.pos['y'] >= screenHeight - parseInt(ballStyle.height, 10) / 2) {
        ball.angle = - ball.angle;
    }
    // normAngle(ball.angle);
}

// Execute gameLoop every x ms
exampleSocket.addEventListener('open', (event) => {
    const intervalID = setInterval(gameLoop, 1);
});

// Need a function which take the positions from the server.