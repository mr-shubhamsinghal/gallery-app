from django.urls import path

from gallery import views


app_name = 'gallery'

urlpatterns = [
	path('', views.home, name='home'),
	path('add-images', views.add_images, name='add-images'),
	path('load-images', views.load_images, name='load-images'),
	path('tag', views.filter_by_tags, name='tag-filter'),
]
