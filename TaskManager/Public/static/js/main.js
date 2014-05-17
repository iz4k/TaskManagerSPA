$(function(){
	$('.right-up-panel').load('/small_task_list/ .content');
	$(document).on('click', '.ajax', function(){
		$('.left-panel').load($(this).attr('href')+' .content');

		$('.active').removeClass('active');
		$(this).parent('li').addClass('active');
		history.pushState(null, null, $(this).attr('href'));
		return false;
	});

	$(document).on('submit', '#form-group', function(){
		var data =  $(this).serialize();
		$.post('/groups_new/', data, function(){
			history.back();
		})
		.fail(function(data) {
			errorHandle(data);
		});
        return false;
	});


	$(document).on('click', '#del_task', function(e){
		var task_id = e.target.getAttribute("data-id");
		$("#tmodal").one("hidden.bs.modal", function(){
			$.post('/delete_task/', {"id":task_id}, function(response){
				$('.left-panel').load("/tasks/" +" .content")
			})
			.fail(function(data){
				errorHandle(data);
			});
		});
	});

	$(document).on('click', '#del_group', function(e){
		var group_id = e.target.getAttribute("data-id");
		$("#gmodal").one("hidden.bs.modal", function(){
			$.post('/delete_group/', {"id":group_id}, function(response){
				$('.left-panel').load("/groups/" +" .content")
			})
			.fail(function(data){
				errorHandle(data);
			});
		});
	});

	$(document).on('click', '#del_comment', function(e){
		var comment_id = e.target.getAttribute("data-id");
		$("#cmodal"+comment_id).one("hidden.bs.modal", function(){
			$.post('/delete_comment/', {"id":comment_id}, function(response){
				$('.left-panel').load(response + ' .content');
			})
			.fail(function(data){
				errorHandle(data);
			});
		});		
	});


	$(document).on('submit', '#form-task', function(){
		$.post('/tasks_new/', $(this).serialize(), function(){
			history.back();
			$('#calendar').fullCalendar( 'refetchEvents' );
		})
		.fail(function(data) {
			errorHandle(data);
		});
        return false;
	});

	$(document).on('submit', '#form-comment', function(){
		var id = $('#form-comment').attr("nro");
		var variety = $('#form-comment').attr("variety");
		var url = '/'+variety+'/'+id+'/';
		$.post(url, $(this).serialize(), function(){
			$('.left-panel').load(url + ' .content');
		})

		.fail(function(data) {
			errorHandle(data);

		});
        return false;
	});

	window.onpopstate = function(event) {
		$('.left-panel').load(location.pathname+' .content');
	}

	function errorHandle (data) {
		var errors = $.parseJSON(data.responseText);
		for (error in errors) {
		var id = '#id_' + error;
			$(id).parent('div').append(errors[error]);
		}
	}

	// Calendar initialization
	$('#calendar').fullCalendar({
		height: 380,
		events: function(start, end, callback) {
    	    $.ajax({
				url: '/calendarjson/',
				dataType: 'json',
				data: {
					// our hypothetical feed requires UNIX timestamps
					start: Math.round(start.getTime() / 1000),
					end: Math.round(end.getTime() / 1000)
				},
				success: function(doc) {
					var events = [];
					$(doc).each(function() {
						events.push({
							title: $(this).attr('title'),
							start: $(this).attr('start'),
							url: $(this).attr('url'),
							backgroundColor : $(this).attr('bgColor'),
							textColor: 'black' 
						});
					});
					callback(events);
				}
			});
		},
		eventClick: function(event) {
			$('.left-panel').load(event.url+' .content');

			history.pushState(null, null, $(this).attr('href'));
			return false;
		}
	});

	$.ajaxSetup({ 
	     beforeSend: function(xhr, settings) {
	         function getCookie(name) {
	             var cookieValue = null;
	             if (document.cookie && document.cookie != '') {
	                 var cookies = document.cookie.split(';');
	                 for (var i = 0; i < cookies.length; i++) {
	                     var cookie = jQuery.trim(cookies[i]);
	                     // Does this cookie string begin with the name we want?
	                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                     break;
	                 }
	             }
	         }
	         return cookieValue;
	         }
	         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
	             // Only send the token to relative URLs i.e. locally.
	             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	         }
	     } 
	});


});




