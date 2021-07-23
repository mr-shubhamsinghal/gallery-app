var tag_filter = 0;
var tag_name;

$('.tag-class').click(function(e) {
	var tag = $(this).text();
	$('.tag-class').removeClass('btn-dark');
	$(this).addClass('btn-dark');
	tag_name = tag;
	$.ajax({
		url: '/tag/' + tag
	}).done(function(res) {
		tag_filter = 1;
		$('#gallery').html(res);
	});
});

$('#clear-tag').click(function(e) {
	$('.tag-class').removeClass('btn-dark');
	window.location.reload('/');
});
