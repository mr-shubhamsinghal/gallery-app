$('.tag-class').click(function(e) {
	var tag = $(this).text();
	$.ajax({
		url: '/tag/' + tag
	}).done(function(res) {
		$('#gallery').html(res);
	});
});

// $('.page-number').click(function(e) {
// 	var p_num = $(this).text();
// 	$.ajax({
// 		url:  
// 	})
// })
