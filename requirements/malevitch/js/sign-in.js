// Input box password filling.

document.querySelector('.sign-in-input').addEventListener('input', function() {
	var	container = this.closest('.sign-in-input-container');
	var	warning = document.querySelector('.sign-in-input-warning');
	
	if (this.value.length >  0) {
		container.classList.add('input-container-focused');
		warning.classList.add('visually-hidden');
	} 
	else {
		container.classList.remove('input-container-focused');
	}
});

// Submit password using Enter key.

document.querySelector('.sign-in-input').addEventListener('keypress', function(event) {
	if (event.key === 'Enter' && this.value.length > 0) {
		submitPassword(this.value);
	}
});

// Submit password using button.

document.querySelector('.sign-in-submit').addEventListener('click', function() {
	var	input = document.querySelector('.homepage-id-input');

	submitPassword(input.value);
});

// Submit password to database.

async function submitPassword(password) {
	var	id = document.querySelector('.sign-in-message').getAttribute('unique-id');
	var	nickname = document.querySelector('.sign-in-message b').textContent;
	nickname = nickname.trim();

	try {
		const response = await fetch('/petrus/auth/signin/' + nickname, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({id: id, pass: password,}),
		});

		const result = await response.json();

		if ('Err' in result && 'Err' === 'Invalid password') {
			sendInvalidPassword();
		}
		else if ('Err' in result) {
			console.error(result.Err);
		}
		else {
			// switch to homepage.
		}
	}
	catch (error) {
		console.error("Error:", error);
	}
}

// Send warning if password is invalid.

function sendInvalidPassword() {
	var	input = document.querySelector('.sign-in-input');
	var	warning = document.querySelector('.sign-in-input-warning');
	var	locale = document.querySelector('.sign-in-language-selector button img').alt;

	switchLanguageContent(locale);
	warning.classList.remove('visually-hidden');
	input.value = '';
}