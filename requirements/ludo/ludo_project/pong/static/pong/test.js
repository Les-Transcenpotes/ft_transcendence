/***************************************** Setup *****************************************/

let gameArea = document.getElementById("test-target"),
htmlPlayer1 = document.getElementById("player1"),
htmlPlayer2 = document.getElementById("player2"),
htmlBall = document.getElementsByClassName("ball")[0];

const ballStyle = getComputedStyle(htmlBall);
const player1Style = getComputedStyle(htmlPlayer1);
const player2Style = getComputedStyle(htmlPlayer2);

const screenHeight = window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
htmlPlayer2.style.left = screenWidth - parseInt(player1Style.width, 10) - 10 + 'px';


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
        this.angle = 0;
        this.size = screenHeight / 100;
    }
    move() {
        this.pos['x'] += this.speed * Math.cos(this.angle);
        this.pos['y'] -= this.speed * Math.sin(this.angle);
    }
    init() {
        this.pos = {x: screenWidth / 2, y: screenHeight / 2};
        this.speed = screenHeight / 500;
        this.angle = 0;
        this.size = screenHeight / 100;
    }
}

/***************************************** Players movements *****************************************/

let player1 = new Player("player1");
let player2 = new Player("player2");

// Events for keyboard inputs
gameArea.addEventListener("keydown", (e) => { // Booleans with on press and on release (anyway will be a websocket) !!
    if (e.repeat) {
        return;
    }
    if (`${e.key}` === 'ArrowUp') {
        player2.up = true;
    } else if (`${e.key}` === 'ArrowDown') {
        player2.down = true;
    }
    if (`${e.key}` === 'w') {
        player1.up = true;
    } else if (`${e.key}` === 's') {
        player1.down = true;
    }
});

gameArea.addEventListener("keyup", (e) => { // Booleans with on press and on release (anyway will be a websocket) !!
    if (`${e.key}` === 'ArrowUp') {
        player2.up = false;
    } else if (`${e.key}` === 'ArrowDown') {
        player2.down = false;
    }
    if (`${e.key}` === 'w') {
        player1.up = false;
    } else if (`${e.key}` === 's') {
        player1.down = false;
    }
});

/***************************************** Websockets *****************************************/

console.log("ws://" + window.location.host + '/pong/ws/player1/')
const exampleSocket = new WebSocket('ws://localhost:8005/pong/'); // Probably add room name

exampleSocket.onopen = function(event) {
    console.log("Socket opened in the front");
    exampleSocket.send("Socket opened in the front"); // Player names maybe ?
};

exampleSocket.onclose = function() {
    console.log("Socket closed");
}

exampleSocket.onerror = function(event) {
    console.log("Socket error");
}

function sendData(ballPos, player1Pos, player2Pos) {
    // Construct a msg object containing the data the server needs to process the message from the chat client.
    const gameData = {
      ballPos: ballPos,
      player1Pos: player1Pos,
      player2Pos: player2Pos,
    };
  
    // Send the msg object as a JSON-formatted string.
    exampleSocket.send(JSON.stringify(gameData));
}
  
exampleSocket.onmessage = (event) => {
    const f = gameArea.contentDocument;
    let text = "";
    const msg = JSON.parse(event.data);
  
    switch (msg.type) {
      case "id":
        clientID = msg.id;
        setUsername();
        break;
      case "username":
        text = `User <em>${msg.name}</em> signed in at ${timeStr}<br>`;
        break;
      case "message":
        text = `(${timeStr}) ${msg.name} : ${msg.text} <br>`;
        break;
      case "rejectusername":
        text = `Your username has been set to <em>${msg.name}</em> because the name you chose is in use.<br>`;
        break;
    }
};

/***************************************** Game logic *****************************************/

function isPlayerCollision(ball, player, playerStyle) {
    if (ball.pos['y'] > player.pos - (parseInt(playerStyle.height, 10) / 2) && ball.pos['y'] < player.pos + (parseInt(playerStyle.height, 10) / 2)) {
        return true;
    }
    return false;
}

function playerCollision(ball, player, playerStyle) {
    let impactToMid = (ball.pos['y'] - player.pos) / (parseInt(playerStyle.height, 10) * 0.5); // > 0 quand la balle tape en DESSOUS du milieu
    if (player.name === "player1") {
        ball.angle = - (Math.PI / 4) * impactToMid;
    } else if (player.name === "player2") {
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
        player1.points++;
        ball.init();
    } else if (ball.pos['x'] < 0) {
        player2.points++;
        ball.init();
    }
    document.getElementById("score1").innerHTML = player1.points.toString();
    document.getElementById("score2").innerHTML = player2.points.toString();

    // Update positions
    ball.move();
    player1.move(player1Style);
    player2.move(player2Style);

    // Update back
    // sendData(ball.pos, player1.pos, player2.pos);

    // Update front
    htmlBall.style.top = ball.pos['y'] - parseInt(ballStyle.height, 10) / 2 + 'px';
    htmlBall.style.left = ball.pos['x'] - parseInt(ballStyle.width, 10) / 2 + 'px';
    htmlPlayer1.style.top = player1.pos - parseInt(player1Style.height, 10) / 2 + 'px';
    htmlPlayer2.style.top = player2.pos - parseInt(player2Style.height, 10) / 2 + 'px';

    // Collision with player2
    if (ball.pos['x'] >= screenWidth - (parseInt(ballStyle.width, 10) + parseInt(player2Style.width, 10)) && isPlayerCollision(ball, player2, player2Style)) {
        playerCollision(ball, player2, player2Style);
    }

    // Collision with player1
    if (ball.pos['x'] <= parseInt(ballStyle.width, 10) + parseInt(player1Style.width, 10) && isPlayerCollision(ball, player1, player1Style)) {
        playerCollision(ball, player1, player1Style);
    }

    // Collision with walls
    if (ball.pos['y'] <= parseInt(ballStyle.height, 10) / 2 || ball.pos['y'] >= screenHeight - parseInt(ballStyle.height, 10) / 2) {
        ball.angle = - ball.angle;
    }
    // normAngle(ball.angle);
}

// Execute gameLoop every x ms
const intervalID = setInterval(gameLoop, 1);
