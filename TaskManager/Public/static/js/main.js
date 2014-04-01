$(function(){
	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname);
	}

	$(document).on('click', '.ajax', function(){
		$('.left-panel').load($(this).attr('href'));

	
		$('.left-panel').load($(this).attr('href')+' .content');

		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		console.log("#");
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});


	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname);
	}

});


