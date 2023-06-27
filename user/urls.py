from django.urls import include, path
from rest_framework import routers
from .views import CreateBlogs, DeleteBlogs, UpdateBlogs, UserCreation, UserLogin, ApiOverview, BlogView
from user import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ApiOverview.as_view()),
    path('createblogs/', CreateBlogs.as_view()),
    path('blogsview/', BlogView.as_view()),
    path('register/', UserCreation.as_view()),
    path('login/', UserLogin.as_view()),
    path('deleteblogs/<str:pk>/', DeleteBlogs.as_view()),
    path('updateblogs/<str:pk>/', UpdateBlogs.as_view()),
    
]
