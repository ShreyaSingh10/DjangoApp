
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^$', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
]
"""1) url(r'^posts/', include('posts.urls')) this line will ensure that when we type 
address/posts/ it will take us to the page which will contain posts.urls, which 
means it will go to our posts app and go to the file urls.py which we will be creating 
and inside that it will do what has to be done"""
