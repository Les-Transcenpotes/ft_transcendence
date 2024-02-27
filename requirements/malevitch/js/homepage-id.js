// Input box focus.

document.querySelector('.homepage-id-input').addEventListener('focus', function() {
    this.parentNode.classList.add('homepage-id-input-box-focused');
});

document.querySelector('.homepage-id-input').addEventListener('blur', function() {
    this.parentNode.classList.remove('homepage-id-input-box-focused');
});

// Make the submit button appear only when there is text in the input box.

document.querySelector('.homepage-id-input').addEventListener('input', function() {
	var container = this.closest('.homepage-id-input-container');
    if (this.value.length >  0) {
		container.classList.add('homepage-id-input-container-focused');
    } else {
		container.classList.remove('homepage-id-input-container-focused');
    }
});

// Language selector.

document.querySelectorAll('.dropdown-item').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();

		var activeImg = document.querySelector('.homepage-id-language-selector button img');
		var activeImgSrc = activeImg.src;
		var	activeLang = activeImg.alt;
		var selectedImg = this.firstElementChild;
		var	selectedLang = selectedImg.getAttribute('alt');

		switchLanguageAttr(selectedLang, 'placeholder');
		switchLanguageContent(selectedLang);
		activeImg.setAttribute('src', selectedImg.getAttribute('src'));
		activeImg.setAttribute('alt', selectedLang);
		selectedImg.setAttribute('src', activeImgSrc);
		selectedImg.setAttribute('alt', activeLang);
    });
});