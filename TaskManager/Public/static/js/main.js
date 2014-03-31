$(function(){

	$('.navbar-nav li a').click(function(){
		$('.left-panel').load($(this).attr('href') + ' .content');
		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		return false;
	});

});