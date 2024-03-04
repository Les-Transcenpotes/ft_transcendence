// Global variables.
let userId;

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
			var	info;
			if (element.querySelector('b') !== null) {
				info = element.querySelector('b').innerHTML;
				info = info.replace(/\&nbsp;/g, '');
			}
			element.textContent = translations[locale][key];
			if (info && info.trim() !== '') {
				addInfoToElement(info, element);
			}
		}
	  });
	});
}

// Make every language selectors be the same no matter the page.

function switchNextLanguageFromPreviousSelector(previous, next) {
	var	prevSelector = document.querySelector(previous + '-language-selector');
	var	prevSelectorImg = prevSelector.firstElementChild.firstElementChild;
	var	locale = prevSelectorImg.getAttribute('alt');

	var	nextSelector = document.querySelector(next + '-language-selector');
	var	nextSelectorImg = nextSelector.firstElementChild.firstElementChild;

	if (nextSelectorImg.getAttribute('alt') !== locale) {
		var	nextSelectorImgSrc = nextSelectorImg.getAttribute('src');
		var	nextSelectorImgAlt = nextSelectorImg.getAttribute('alt');
		var	nextSelectorButtons = document.querySelectorAll(next + '-language-selector ul li a img');

		nextSelectorImg.setAttribute('src', prevSelectorImg.getAttribute('src'));
		nextSelectorImg.setAttribute('alt', locale);
		if (nextSelectorButtons[0].getAttribute('alt') === locale) {
			nextSelectorButtons[0].setAttribute('src', nextSelectorImgSrc);
			nextSelectorButtons[0].setAttribute('alt', nextSelectorImgAlt);
		}
		else if (nextSelectorButtons[1].getAttribute('alt') === locale) {
			nextSelectorButtons[0].setAttribute('src', nextSelectorImgSrc);
			nextSelectorButtons[0].setAttribute('alt', nextSelectorImgAlt);
		}
	}

	// switchLanguageContent(locale);
	// switchLanguageAttr(locale, 'placeholder');
}

// Language selector : updates the page language / updates the selector images.

document.querySelectorAll('.language-selector-dropdown').forEach(function(item) {
	item.addEventListener('click', function(event) {
		event.preventDefault();

		var	activeImg = this.parentNode;
		while (!activeImg.classList.contains('language-selector'))
			activeImg = activeImg.parentNode;
		activeImg = activeImg.firstElementChild.firstElementChild;
		var	activeImgSrc = activeImg.src;
		var	activeLang = activeImg.alt;
		var	selectedImg = this.firstElementChild;
		var	selectedLang = selectedImg.getAttribute('alt');

		switchLanguageAttr(selectedLang, 'placeholder');
		switchLanguageContent(selectedLang);
		activeImg.setAttribute('src', selectedImg.getAttribute('src'));
		activeImg.setAttribute('alt', selectedLang);
		selectedImg.setAttribute('src', activeImgSrc);
		selectedImg.setAttribute('alt', activeLang);
	});
});

// Input box focus.

document.querySelectorAll('.input').forEach(function(item) {
	item.addEventListener('focus', function() {
		this.parentNode.classList.add('input-box-focused');
	})
});

document.querySelectorAll('.input').forEach(function(item) {
	item.addEventListener('blur', function() {
		this.parentNode.classList.remove('input-box-focused');
	})
});

// Nickname checking functions

function nicknameValidChar(nickname) {
	let regex = /[^A-Za-z0-9_]/g;
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

//

function addInfoToElement(info, element) {
	element.innerHTML = element.textContent + '<b>&nbsp;' + info + '&nbsp;</b>!';
}