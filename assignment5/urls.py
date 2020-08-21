from django.contrib import admin
from django.urls import path
from assignment5 import views

app_name = 'assignment5'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:pos_id>', views.blog_details, name='detail'),
    path('element/', views.element, name='element'),
    path('contact_us/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]