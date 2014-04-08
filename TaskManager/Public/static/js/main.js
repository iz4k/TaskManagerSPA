$(function(){
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

	/* Calendar initialization
	$('#calendar').fullCalendar({
		height: 380,
		events: {
			url: 'http://mikesmithdev.com/feeds/caljson2.ashx', 
			error: function(e) {
				alert('there was an error while fetching events!');
			},
			color: 'yellow',   // a non-ajax option
			textColor: 'black' // a non-ajax option
		}
	});*/
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
});




