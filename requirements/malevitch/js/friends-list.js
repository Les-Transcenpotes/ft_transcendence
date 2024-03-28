document.querySelector('.friends-list-icon').addEventListener('click', function() {
	document.querySelector('.friends-list').classList.add('visually-hidden');

	g_state.pageToDisplay = '.homepage-game';
	window.history.pushState(g_state, null, "");
	render(g_state);
});