function loadTranslations(locale) {
	return fetch('./assets/lang/translations.json')
	  .then(response => response.json())
	  .catch(error => console.error(error));
}

function switchLanguageAttr(locale, newAttr) {
	loadTranslations(locale).then(translations => {
	  document.querySelectorAll('[data-language]').forEach(element => {
		const key = element.getAttribute('data-language');
		element.setAttribute(newAttr, translations[locale][key]);
	  });
	});
}