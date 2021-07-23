from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def make_pages(page, item_list, page_size):

	paginator = Paginator(item_list, page_size)

	try:
		images = paginator.page(int(page))
	except PageNotAnInteger:
		images = paginator.page(1)
	except EmptyPage:
		images = paginator.page(paginator.num_pages)

	return images
