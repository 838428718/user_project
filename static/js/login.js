$(function() {

		$("#submit").click(function() {
			var account = $('#account').val();
			var user_password = $('#password').val();
			$.ajax({
				type:"POST",
				url:"/app/login",
                headers:{"X-CSRFToken":$.cookie('csrftoken')},
                data:{'account':account, 'user_password':user_password},

				success: function(data){
					if(data['status']=='200'){
                        window.location.href="/app/index";
					}
					if(data['status']=='101'){
					    $('.tips').css('visibility','visible');
                    }

				}
			});
		});

	});