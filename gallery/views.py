
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from gallery.models import ImageClass, TagClass
from gallery.utils import make_pages, image_rotate


def home(request):
	tag_list = TagClass.objects.all()
	image_list = ImageClass.objects.all()
	page = json.loads(request.GET.get('page', '1'))
	images = load_pages(image_list, page)
	context = {'tags': tag_list, 'images': images}
	return render(request, 'home.html', context)


def load_pages(data_list, page):
	page_size = 8
	images = make_pages(page, data_list, page_size)
	return images


def load_images(request):
	page = json.loads(request.GET.get('page', '1'))
	image_list = ImageClass.objects.all()
	images = load_pages(image_list, page)
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


def filter_by_tags(request):
	tag_list = json.loads(request.GET.get('tag_list', []))
	page = json.loads(request.GET.get('page', '1'))
	image_list = ImageClass.objects.filter(tags__tag_name=tag_list[0])
	n = len(tag_list)
	for index in range(1, n):
		image_list = image_list.filter(tags__tag_name=tag_list[index])
	images = load_pages(image_list, page)
	context = {'images': images}
	return render(request, 'gallery.html', context)


def image_preview(request, image_url):
	context = {'image_url': image_url}
	return render(request, 'image_preview.html', context)


def rotate_image(request):
	angle = json.loads(request.GET.get('angle'))
	image_url = request.GET.get('image_url')
	image_rotate(image_url, angle)
	return HttpResponse('')
