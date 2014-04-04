$(function(){



	$(document).on('click', '.ajax', function(){
	
		$('.left-panel').load($(this).attr('href')+' .content');

		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});

	$(document).on('submit', '#form-group', function(){
		$.post('/groups_new/', $(this).serialize(), function(){
			$('.left-panel').load('/groups/ .content');
		});
        return false;
	});

	$(document).on('submit', '#form-task', function(){
		$.post('/tasks_new/', $(this).serialize(), function(){
			$('.left-panel').load('/tasks/ .content');
		});
        return false;
	});

	$(document).on('submit', '#form-comment', function(){
		var id = $('#form-comment').attr("nro");
		var variety = $('#form-comment').attr("variety");
		var url = '/'+variety+'/'+id+'/';
		$.post(url, $(this).serialize(), function(){
			$('.left-panel').load(url + ' .content');
		});
        return false;
	});


	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname+' .content');
	}


});


