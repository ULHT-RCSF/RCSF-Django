from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gsm/', views.gsm, name='gsm'),
    path('espaco_livre', views.espaco_livre, name="espaco_livre")
]
