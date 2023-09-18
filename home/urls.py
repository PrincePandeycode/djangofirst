from django.contrib import admin
from django.urls import path,include
from home import views
 

#Django admin header customization

admin.site.site_header = "Developer Prince"
admin.site.site_title = "welcome to my dashboard"
admin.site.index_title = "welcome to this portal"
urlpatterns = [
    path('home', views.home, name='home'),
    path('projects',views.control, name = 'projects'),
    path('about', views.about, name = 'about'),
    path('contact',views.contact, name = 'contact')
]
