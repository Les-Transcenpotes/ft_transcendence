// Translation functions.

function loadTranslations() {
	return fetch('./assets/lang/translations.json')
	  .then(response => response.json())
	  .catch(error => console.error(error));
}

function switchLanguageAttr(locale, newAttr) {
	loadTranslations().then(translations => {
	  document.querySelectorAll('[data-language]').forEach(element => {
		const key = element.getAttribute('data-language');
		if (element.hasAttribute(newAttr)) {
			element.setAttribute(newAttr, translations[locale][key]);
		}
	  });
	});
}

function switchLanguageContent(locale) {
	loadTranslations().then(translations => {
	  document.querySelectorAll('[data-language]').forEach(element => {
		const key = element.getAttribute('data-language');
		if (element.textContent.trim() !== '') {
			element.textContent = translations[locale][key];
		}
	  });
	});
}

// Parsing functions

function nicknameValidChar(nickname) {
	let regex = /[^A-Za-z0-9-_]/g;
	return !regex.test(nickname);
}

function isNicknameValid(nickname, element) {
	if (nicknameValidChar(nickname) === false) {
		element.setAttribute('data-language', 'nickname-invalid-char');
		return false;
	}
	else if (nickname.length < 3) {
		element.setAttribute('data-language', 'nickname-too-short');
		return false;
	}
	else if (nickname.length > 15) {
		element.setAttribute('data-language', 'nickname-too-long');
		return false;
	}
	return true;
}