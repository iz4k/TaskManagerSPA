$(function(){

	$('.ajax').click(function(){
		$('.left-panel').load($(this).attr('href'));
		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		return false;
	});

});