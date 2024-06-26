from django.urls import path
from . import views

urlpatterns = [
    path('admin_site/<str:title>', views.main_admin, name='admin_site'),
    path('contact/<str:title>', views.main_contact, name='contact'),
    path('facts/<str:title>', views.main_facts, name='facts'),
    path('/<str:title>', views.main_page, name='main'),
    path('news/<str:title>', views.news_page, name='news'),
    path('history/people/<str:title>', views.history_page, name='history'),
    path('history/photos/<str:title>', views.history_page, name='history'),

    path('admin_site/', views.main_admin, name='admin_site'),
    path('contact/', views.main_contact, name='contact'),
    path('facts/', views.main_facts, name='facts'),
    path('', views.main_page, name='main'),
    path('news/', views.news_page, name='news'),
    path('history/', views.history_page, name='history'),
    path('history/people', views.people_page, name='people'),
    path('history/photos', views.photos_page, name='photos'),
]

""" TODO: nefunguje mi toto omezení na hlavní stránku a na history site - takze stranky
   http://127.0.0.1:8000/history/blbost nebo http://127.0.0.1:8000/blbost vykazuji chybu - jak to opravit?"""