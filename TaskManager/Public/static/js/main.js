$(function(){

	$('.ajax').click(function(){
		$('.left-panel').load($(this).attr('href'));
		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});

});