from django.urls import path

from gallery import views


app_name = 'gallery'

urlpatterns = [
	path('', views.home, name='home'),
	path('add-images', views.add_images, name='add-images'),
	path('tag/<str:name>', views.filter_by_tags, name='tag-filter'),
]
