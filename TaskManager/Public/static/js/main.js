$(function(){
	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname);
	}

	$('.ajax').click(function(){
		$('.left-panel').load($(this).attr('href')+' .content');
		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});

});