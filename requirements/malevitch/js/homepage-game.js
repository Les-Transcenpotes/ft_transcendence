document.querySelector('.homepage-game-content-friends-icon').addEventListener('click', function() {
	document.querySelector('.homepage-game').classList.add('visually-hidden');

	g_state.pageToDisplay = '.friends-list';
	window.history.pushState(g_state, null, "");
	render(g_state);
});