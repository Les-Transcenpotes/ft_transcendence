/***************************************** Setup *****************************************/

let textarea = document.getElementById("test-target"),
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
    }
    move(mvt, playerStyle) {
        const newPos = this.pos + mvt * screenHeight / 100;
        if (newPos + parseInt(playerStyle.height, 10) / 2 < screenHeight && newPos > parseInt(playerStyle.height, 10) / 2) {
            this.pos = newPos;
        }
    }
}

class Ball {
    constructor() {
        this.pos = {x: screenWidth / 2, y: screenHeight / 2};
        this.speed = screenHeight / 500;
        this.angle = Math.PI / 15;
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
textarea.addEventListener("keydown", (e) => { // Booleans with on press and on release (anyway will be a websocket) !!
    if (`${e.key}` === 'ArrowUp') {
        player2.move(-1, player2Style);
    } else if (`${e.key}` === 'ArrowDown') {
        player2.move(1, player2Style);
    }
    if (`${e.key}` === 'w') {
        player1.move(-1, player1Style);
    } else if (`${e.key}` === 's') {
        player1.move(1, player1Style);
    }
});

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
        if (ball.angle > 0) {
            ball.angle += Math.PI - 2 * ball.angle - ((Math.PI / 4) * impactToMid);
        } else {
            ball.angle += - Math.PI - 2 * ball.angle + ((Math.PI / 4) * impactToMid);
        }
    }
    else if (player.name === "player2") {
        if (ball.angle > 0) {
            ball.angle += Math.PI - 2 * ball.angle + ((Math.PI / 4) * impactToMid);
        } else {
            ball.angle += - Math.PI - 2 * ball.angle - ((Math.PI / 4) * impactToMid);
        }
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
