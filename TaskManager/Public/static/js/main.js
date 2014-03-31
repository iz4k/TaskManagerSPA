$(function(){

	$('.navbar-nav li a').click(function(){
		$('.left-panel').load($(this).attr('href') + ' .content');
		return false;
	});

});