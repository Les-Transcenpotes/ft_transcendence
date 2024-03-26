document.querySelector('.homepage-header-logo').addEventListener('click', function() {
	document.querySelector('.homepage-game-picture').classList.remove('visually-hidden');

	var	currentPage = g_state.pageToDisplay;

	g_state.pageToDisplay = '.homepage-game';
	
	if (currentPage != '.homepage-game') {
		window.history.pushState(g_state, null, "");
	}
	render(g_state);
});