// Input box focus.

document.querySelector('.homepage-id-input').addEventListener('focus', function() {
    this.parentNode.classList.add('homepage-id-input-box-focused');
});

document.querySelector('.homepage-id-input').addEventListener('blur', function() {
    this.parentNode.classList.remove('homepage-id-input-box-focused');
});

// Input box filling.

document.querySelector('.homepage-id-input').addEventListener('input', function() {
	var	container = this.closest('.homepage-id-input-container');
	var	warning = document.querySelector('.homepage-id-warning');
	var locale = document.querySelector('.homepage-id-language-selector button img').alt;

    if (this.value.length >  0) {
		// Make the submit button appear only when there is text in the input box.
		container.classList.add('homepage-id-input-container-focused');

		// Warn and block invalid characters, or nicknames too short or too long.
		if (isNicknameValid(this.value, warning) === false) {
			switchLanguageContent(locale);
			warning.classList.remove('visually-hidden');
		}
		else {
			warning.classList.add('visually-hidden');
		}
    } 
	else {
		container.classList.remove('homepage-id-input-container-focused');
		warning.classList.add('visually-hidden');
    }
});

// Language selector : updates the page language / updates the selector images.

document.querySelectorAll('.language-selector-dropdown').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();

		var	activeImg = document.querySelector('.homepage-id-language-selector button img');
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