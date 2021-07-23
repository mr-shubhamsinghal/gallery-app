var tag_filter = 0;
var tags_list = [];

$('.tag-class').click(function(e) {
	var tag = $(this).text();
	$(this).addClass('btn-dark');
	tags_list.push(tag);

	$.ajax({
		url: '/tag',
		data: {tag_list: JSON.stringify(tags_list)}
	}).done(function(res) {
		tag_filter = 1;
		$('#gallery').html(res);
	});
});

$('#clear-tag').click(function(e) {
	$('.tag-class').removeClass('btn-dark');
	window.location.reload('/');
});
