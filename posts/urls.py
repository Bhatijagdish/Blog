from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
]