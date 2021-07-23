
import json

from django.shortcuts import render, redirect
from gallery.models import ImageClass, TagClass
from gallery.utils import make_pages


def home(request):
	tag_list = TagClass.objects.all()
	context = {'tags': tag_list}
	return render(request, 'home.html', context)


def load_images(request):
	image_list = ImageClass.objects.all()
	page = json.loads(request.GET.get('page', '1'))
	page_size = 8
	images = make_pages(page, image_list, page_size)
	context = {'images': images}
	return render(request, 'gallery.html', context)


def add_images(request):
	if request.method == 'POST':
		images = request.FILES.getlist('images')
		tag_list = request.POST.getlist('tags')

		for image in images:
			image_obj = ImageClass(image=image)
			image_obj.save()
			image_obj.tags.set(tag_list)
			image_obj.save()
	return redirect('/')


def filter_by_tags(request, name):
	page = request.GET.get('page', 1)
	page_size = 8
	image_list = ImageClass.objects.filter(tags__tag_name=name)
	images = make_pages(page, image_list, page_size)
	context = {'images': images}
	return render(request, 'gallery.html', context)
