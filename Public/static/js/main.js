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
			$('.right-up-panel').load('/small_task_list/');
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
						//if ($(this).attr('title') == 'More...')
							// it is working alert('One More option here');
						events.push({
							title: $(this).attr('title'),
							start: $(this).attr('start')+1,
							url: $(this).attr('url'),
							backgroundColor : $(this).attr('bgColor'),
							textColor: 'black' 
						});
					});
					callback(events);
				}
			});
		},
		eventMouseover: function(event, jsEvent, view) {
			var left = $(this).css('left').split("px");
			var top = $(this).css('top').split("px");
			left = parseInt(left[0]) - 2;
			top = parseInt(top[0]) + 18;
			if (event.title == "More...") {
				$(".box_event_outer").remove();
				var test = String(event.start);
				test = test.split(' ');
				if (test[1] == "Jan")
					test[1] = '01';
				else if (test[1] == "Feb")
					test[1] = '02';
				else if (test[1] == "Mar")
					test[1] = '03';
				else if (test[1] == "Apr")
					test[1] = '04';
				else if (test[1] == "May")
					test[1] = '05';
				else if (test[1] == "Jun")
					test[1] = '06';
				else if (test[1] == "Jul")
					test[1] = '07';
				else if (test[1] == "Aug")
					test[1] = '08';
				else if (test[1] == "Sep")
					test[1] = '09';
				else if (test[1] == "Oct")
					test[1] = '10';
				else if (test[1] == "Nov")
					test[1] = '11';
				else if (test[1] == "Dec")
					test[1] = '12';
				$.get("/calendarmore/"+test[3]+"/"+test[1]+"/"+test[2]+"/",function(data) {
					$(".fc-event-container").append(data);
					$(".box_event_outer").css('top', top);
					$(".box_event_outer").css('left', left);
				});
			}
        },
		eventClick: function(event) {
			if (event.title != "More...") {
				$('.left-panel').load(event.url+' .content');
				history.pushState(null, null, $(this).attr('href'));
			} 
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


	$(".inner-div").on( "mouseleave", function() {
		$(".box_event_outer").remove();
	});

});




