from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:id>', views.post, name='post'),
    path('post/<str:id>/add_comment', views.add_comment, name='add_comment'),
    path('like/<str:id>', views.my_like, name='my_like'),
]
