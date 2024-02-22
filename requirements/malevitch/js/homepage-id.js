document.querySelector('.homepage-id-input').addEventListener('focus', function() {
    this.parentNode.classList.add('homepage-id-input-box-focused');
});

document.querySelector('.homepage-id-input').addEventListener('blur', function() {
    this.parentNode.classList.remove('homepage-id-input-box-focused');
});

document.querySelector('.homepage-id-input').addEventListener('input', function() {
	var container = this.closest('.homepage-id-input-container');
    if (this.value.length >  0) {
		container.classList.add('homepage-id-input-container-focused');
    } else {
		container.classList.remove('homepage-id-input-container-focused');
    }
});

document.querySelectorAll('.dropdown-item').forEach(function(item) {
    item.addEventListener('click', function(event) {
        event.preventDefault();
        var button = document.querySelector('.homepage-id-language-selector button');
		var activeLangAttr = button.getAttribute('lang');
		var activeLangUrl = window.getComputedStyle(button).getPropertyValue('background-image');
		var selectedLangAttr = this.getAttribute('lang');
		var selectedLangUrl;
		if (selectedLangAttr === 'fr') {
			selectedLangUrl = 'url(./assets/general/flag-france.png)';
		}
		else if (selectedLangAttr === 'zh') {
			selectedLangUrl = 'url(./assets/general/flag-china.png)';
		}
		else {
			selectedLangUrl = 'url(./assets/general/flag-unitedkingdom.png)';
		}
		console.log(activeLangAttr + ' ' + activeLangUrl + ' ' + selectedLangAttr + ' ' + selectedLangUrl);
        button.style.backgroundImage = selectedLangUrl;
		button.setAttribute('lang', selectedLangAttr);
		this.setAttribute('lang', activeLangAttr);
		this.style.backgroundImage = activeLangUrl;
    });
});