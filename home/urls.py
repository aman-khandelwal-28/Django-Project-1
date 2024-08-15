from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization
admin.site.site_header = "Login to my Portfolio"
admin.site.site_title = "Welcome to my Portfolio"
admin.site.index_title = "Welcome again!"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
]