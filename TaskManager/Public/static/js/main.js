$(function(){
	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname+' .content');
	}

	$(document).on('click', '.ajax', function(){
	
	
		$('.left-panel').load($(this).attr('href')+' .content');

		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		console.log($(this).attr('href'));
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});

});


