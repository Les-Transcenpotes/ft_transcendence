document.querySelector('.sign-in-input').addEventListener('input', function() {
	var	container = this.closest('.sign-in-input-container');
	
	if (this.value.length >  0) {
		container.classList.add('input-container-focused');
	} 
	else {
		container.classList.remove('input-container-focused');
	}
});