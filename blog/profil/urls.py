from django.urls import path
from profil import views
from .views import contact_view

urlpatterns = [
         path('', views.home, name='home'),
         path('tambah/', views.form_barang, name='tambah'),
         path('contact/', contact_view, name='contact'),
         path('contact/', views.contact_view, name='contact'),
]
