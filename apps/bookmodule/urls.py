from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),                 # Template (Task 4/5)
    path('hello/', views.index),          # Task 1/2 (HttpResponse)
    path('index2/text/', views.index2_text),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
]
