class connectionPage extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        const template = document.getElementById('connection-page-t');
        const clone = template.content.cloneNode(true);
        this.shadowRoot.appendChild(clone);
    }
}

customElements.define('connection-page', connectionPage);

function getCookie(name) {
    let cookieValue = null;
    const cookies = document.cookie.split(';');
    console.log(cookies);
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
    return cookieValue;
}

class originalDiv extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        const csrftoken = getCookie('csrftoken');
        console.log(csrftoken);
        fetch('http://localhost:8002/check-authentication/', {
            headers: {
                'X-CSRFToken': csrftoken,
            },
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            if (data.isAuthenticated) {
                this.shadowRoot.innerHTML = `<home-page pseudo=${data.pseudo}></home-page>`;
            } else {
                this.shadowRoot.innerHTML = '<authentication-page></authentication-page>';
                console.log("authentication-page loaded");
                this.shadowRoot.querySelector('authentication-page').addEventListener('authenticated', () => {
                    this.shadowRoot.innerHTML = `<home-page></home-page>`;
                });
            }
        })
        .catch(error => {
            console.error('An error occured:', error);
        });
    }
}

customElements.define('original-div', originalDiv);

class csrfToken extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        fetch('http://localhost:8002//', {
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
    }
}

class authenticationPage extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    getHtml() {
        return '<div>\
            <ul>\
                <li>\
        	        <label for="name">Pseudo\t:    </label>\
        	        <input type="text" id="username" name="username" />\
        	    </li>\
        	    <li>\
        	        <label for="mail">Password\t:</label>\
        	        <input type="email" id="password" name="password" />\
        	    <li>\
        	        <label for="msg">Message&nbsp;:</label>\
        	        <textarea id="msg" name="user_message"></textarea>\
                </li>\
        	    </li>\
                <li>\
                    <div class="button" id=\'button_login\'>\
                        <button>Envoyer le message</button>\
                    </div>\
                </li>\
                <p id="notification"></p>\
            </ul>\
        </div>';
    }

    connectedCallback() {
        this.shadowRoot.innerHTML = this.getHtml();
        this.shadowRoot.querySelector('#button_login').addEventListener('click', async (event) => {
            event.preventDefault();

            const username = this.shadowRoot.querySelector('#username').value;
            const password = this.shadowRoot.querySelector('#password').value;

            if (username == "" || password == "") {
                console.log("No default values");
                return ;
            }

            const data = {
                username: username,
                password: password
            };
            console.log(data);

            try {
                const csrftoken = getCookie('csrftoken');
                const response = await fetch('http://localhost:8002/login/', {
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    method: 'POST',
                    body: JSON.stringify(data),
                    credentials: 'include'
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.isAuthenticated);
                    //if (data.isAuthenticated) {
                    if (true) {
                        this.dispatchEvent(new CustomEvent('authenticated'));
                        console.log("here");
                    }
                    else
                        this.shadowRoot.querySelector("#notification").innerHTML = "can't connect cause of " + data.reason;
                    return ;
                });
            } catch (error) {
                console.log('Error :', error);
            }
        });

    }
}

customElements.define('authentication-page', authenticationPage);

class homePage extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    launchGame() {
        console.log("this");
        this.querySelector("#home-page-main").innerHTML = '<p>yes<p>';
    }

    connectedCallback() {
        this.shadowRoot.innerHTML = this.getHtml();

        this.shadowRoot.querySelector("#Classique").addEventListener('click', this.launchGame);
    }

    getHtml() {
        return `\
        <header>\
            <nav>\
                <ul>\
                    <p>Hello, ${this.pseudo}</p>\
                    <p id="Classique">Classique</p>\
                    <p id="Tournoi>Tournoi</p>\
                    <p id="Stats>Stats</p>\
                    <p id="Logout>Se déconnecter</p>\
                </ul>\
            </nav>\
        </header>\
        <main id="home-page-main">\
            <game></game>\
        </main>`;
    }
}

customElements.define('home-page', homePage);
