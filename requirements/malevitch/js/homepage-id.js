// Input box nickname filling.

document.querySelector('.homepage-id-input').addEventListener('input', function() {
	var	container = this.closest('.homepage-id-input-container');
	var	warning = document.querySelector('.homepage-id-input-warning');
	var	locale = document.querySelector('.homepage-id-language-selector button img').alt;
	
	if (this.value.length > 0) {
		// Make the submit button appear only when the choosen nickname is valid.
		// Warn and block invalid characters, or nicknames too short or too long.
		if (!warnInvalidNickname(this.value, warning)) {
			switchLanguageContent(locale);
			warning.classList.remove('visually-hidden');
			container.classList.remove('input-container-focused');
		}
		else {
			warning.classList.add('visually-hidden');
			container.classList.add('input-container-focused');
		}
	} 
	else {
		warning.classList.add('visually-hidden');
		container.classList.remove('input-container-focused');
	}
});

// Submit nickname using Enter key.

document.querySelector('.homepage-id-input').addEventListener('keypress', function(event) {
	var	warning = document.querySelector('.homepage-id-input-warning');

	if (event.key === 'Enter' && warnInvalidNickname(this.value, warning)) {
		submitNickname(this.value);
	}
});

// Submit nickname using button.

document.querySelector('.homepage-id-submit').addEventListener('click', function() {
	var	input = document.querySelector('.homepage-id-input');

	submitNickname(input.value);
});

// Submit nickname and redirect to signin or signup.

function submitNickname(nickname) {
	var	next;

	document.querySelector('.homepage-id').classList.add('visually-hidden');

	fetch('/petrus/auth/signin/' + nickname)
		.then (response => {
			if (!response.ok) {
				throw new Error('HTTP error: ' + response.status);
			}
			return response.json();
		})
		.then (data => {
			if (data.Ava) {
				next = '.sign-up';
				getSignUpNickname(nickname);
			}
			else {
				next = '.sign-in';
				userId = data.Id;
			}
			document.querySelector(next).classList.remove('visually-hidden');
			next = next.replace('.', '');
			// history.pushState({ path: next }, null, next);
		})
		.catch (error => {
			console.error('Fetch problem:', error.message);
		});

	switchNextLanguageFromPreviousSelector('.homepage-id', '.sign-in');
	addInfoToElement(nickname, document.querySelector('.sign-in-message'));
}