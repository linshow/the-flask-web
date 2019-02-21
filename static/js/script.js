$(function(){
	$('button').click(function(){
		var user = $('#txtUsername').val();
		var pass = $('#txtPassword').val();
		$.ajax({
			url: '/keyAddress',
			data: $('form').serialize(),
			type: 'POST',
			success: function(data){
				console.log(data);
				// $('#successAlert').text(data.user).show();
		
			},
			error: function(error){
				console.log(error);
			}
		}).done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				// $('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.user).show();
				// $('#errorAlert').hide();
			}

		});
	});
});