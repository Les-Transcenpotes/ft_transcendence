// Back to homepage

document.querySelector('.homepage-header-logo').addEventListener('click', function() {
	document.querySelector('.homepage-game-picture').classList.remove('visually-hidden');

	var	currentPage = g_state.pageToDisplay;

	g_state.pageToDisplay = '.homepage-game';
	
	if (currentPage != '.homepage-game') {
		window.history.pushState(g_state, null, "");
	}
	render(g_state);
});

// Display header menus

document.querySelector('.homepage-header-tournaments').addEventListener('click', function() {
	document.querySelectorAll('.homepage-header-open-menu').forEach(function(item) {
		if (!item.classList.contains('homepage-header-open-tournaments')) {
			item.classList.add('visually-hidden');
		}
	});
	document.querySelector('.homepage-header-open-tournaments').classList.toggle('visually-hidden');
});

document.querySelector('.homepage-header-play').addEventListener('click', function() {
	document.querySelectorAll('.homepage-header-open-menu').forEach(function(item) {
		if (!item.classList.contains('homepage-header-open-play')) {
			item.classList.add('visually-hidden');
		}
	});
	document.querySelector('.homepage-header-open-play').classList.toggle('visually-hidden');
});

document.querySelector('.homepage-header-friends').addEventListener('click', function() {
	document.querySelectorAll('.homepage-header-open-menu').forEach(function(item) {
		if (!item.classList.contains('homepage-header-open-friends')) {
			item.classList.add('visually-hidden');
		}
	});
	document.querySelector('.homepage-header-open-friends').classList.toggle('visually-hidden');
});

// Close menus on click outside

function isHeaderOpenMenu(target) {
	var	temp = target;
	if (target.ClassList && target.ClassList.contains('homepage-header-open-menu')) {
		return true;
	}
	while(target.parentNode && target.parentNode.nodeName.toLowerCase() != 'body') {
		var	parentClassList = target.parentNode.classList;
		if (parentClassList && parentClassList.contains('homepage-header-open-menu')) {
			return true;
		}
		target = target.parentNode;
	}
	target = temp;
	if (target.classList && target.classList.contains('homepage-header-menu-button')) {
		return true;
	}
	while(target.parentNode && target.parentNode.nodeName.toLowerCase() != 'body') {
		var	parentClassList = target.parentNode.classList;
		if (parentClassList && parentClassList.contains('homepage-header-menu-button')) {
			return true;
		}
		target = target.parentNode;
	}
	return false;
}

window.addEventListener('click', function ({target}){
	if (!isHeaderOpenMenu(target)) {
		document.querySelectorAll('.homepage-header-open-menu').forEach(function(item) {
			if (!item.classList.contains('visually-hidden')) {
				item.classList.add('visually-hidden');
			}
		});
	}
});