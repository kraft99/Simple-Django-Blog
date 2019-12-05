function getCookie(name) {
        // Function to get any cookie available in the session.
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    function csrfSafeMethod(method) {
        // These HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    var page_title = $(document).attr("title");
    // This sets up every ajax call with proper headers.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

/*ready doc*/
$(document).ready(function(){

	/*reply toggle forms*/

	$('.share-links-wrap .share-link').click(function(e){
		e.preventDefault();
		$('.links-to-social').fadeToggle();
	});

	console.log("we dey");

	$('.links-to-social .click-to-copy').click(function(e){
	e.preventDefault();	
	})

	$("#like-form").submit(function(e){

	e.preventDefault();
	if($(this).hasClass('auth-modal')){
			//  invoke social-auth modal  
			alert("auth with facebook,twitter,google-plus,github,linkedlin");
	}
	else{

		let btn = $('button').filter('.like-btn')[0];
		let post_id = $(this).find("input[type=hidden]").filter(".post_id")[0].value;
		let username = $.trim($(this).find("input[type=hidden]").filter(".username")[0].value);
		let counter = $('span.like-counter')[0];
		let prev_count = counter.textContent;
		const like_url = $(this).attr('action');

		let request_data = {
			'post-id':post_id,
			'username':username,
			'csrf_token': csrftoken
		}
		
		$.ajax({
		url : like_url,
		data: request_data,
		type: 'POST',
		cache: false,
		success : function(response){
			if(response.is_liked == true){
				btn.textContent = "UnLike"
				counter.textContent = parseInt(prev_count) + 1;
			}
			else{
				btn.textContent = "Like"
				counter.textContent = parseInt(prev_count) - 1;
			}
		},

		});
		return false;
	  }/*end else */

	})

});