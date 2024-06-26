from django.urls import path
from . import views

urlpatterns = [
    path('admin_site/', views.main_admin, name='admin_site'),
    path('contact/', views.main_contact, name='contact'),
    path('facts/', views.main_facts, name='facts'),
    path('', views.main_page, name='main'),
    path('news/', views.news_page, name='news'),

]