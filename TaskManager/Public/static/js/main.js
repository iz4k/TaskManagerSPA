$(function(){

	$(document).on('click', '.ajax', function(){
		$('.left-panel').load($(this).attr('href'));
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


