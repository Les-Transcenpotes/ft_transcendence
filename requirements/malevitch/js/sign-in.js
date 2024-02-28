function addNicknameToSignInMessage(nickname) {
	var	message = document.querySelector('.sign-in-message');
	message.textContent = message.textContent + nickname + ' !';
}