from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializer import UserSerializer, GroupSerializer, BlogSerializer, LoginSerilaizer
from rest_framework import viewsets, permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blogs
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ApiOverview(APIView):
    def get(self, request):
        list_of_api={
            "register": "/register/",
            "login": "/login/",
            "createblogs":"/createblogs/",
            "deleteblogs":"/deleteblogs/<str:pk>/",
            "updateblogs":"/updateblogs/<str:pk>/",
        }
        return Response(list_of_api)




class UserCreation(APIView):
    def get(self, requset):
        serializers = UserSerializer()
        return Response(serializers.data)
    def post(self, request):
        user_resgister = UserSerializer(data = request.data)
        if user_resgister.is_valid():
            user_resgister.save()
            return Response(user_resgister.data)
        return Response(user_resgister.errors)

class UserLogin(APIView):
    def post(self, request):
        login = LoginSerilaizer(data=request.data)
        if login.is_valid():
            username = login.data.get("username")
            password = login.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                return Response(login.data)
            return Response({"error": "Invalid Credentials"})
        return Response({"success": "user login successfully" })  
        


class CreateBlogs(LoginRequiredMixin, APIView):
    def get(self, request):
        blogform = Blogs.objects.all()
        serializers = BlogSerializer(blogform, many=True)
        return Response(serializers.data)
        
    def post(self, request):
        blogform = BlogSerializer(data=request.data)
        if blogform.is_valid():
            blogform.save()
            return Response(blogform.data)

class DeleteBlogs(LoginRequiredMixin, APIView):
    def delete(self, request, pk):
        blog = Blogs.objects.filter(id=pk)
        blog.delete()
        blogform = Blogs.objects.all()
        serializers = BlogSerializer(blogform, many=True)
        return Response(serializers.data)
    
class UpdateBlogs(LoginRequiredMixin, APIView):
    def get(self, request, pk):
        blogform = Blogs.objects.filter(id=pk)
        serializers = BlogSerializer(blogform, many=True)
        return Response(serializers.data)
    
    def patch(self, request, pk):
        blog = Blogs.objects.get(id=pk)
        blogform = BlogSerializer(data=request.data, instance=blog)
        if blogform.is_valid():
            blogform.save()
            return Response(blogform.data)
        