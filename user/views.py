from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializer import UserSerializer, GroupSerializer, BlogSerializer, LoginSerilaizer
from rest_framework import viewsets, permissions, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blogs
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    
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
                serializer = UserSerializer(user)
                tokens = get_tokens_for_user(user) 
               
                return Response(
                   {"token":tokens, "msg":"login Success", "user_data": serializer.data}
               )
            
            return Response({"error": "Invalid Credentials"})

        return Response({"success": "user login successfully"})  
        


class CreateBlogs(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes=[IsAuthenticated]
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

# Using generic class-based views
from rest_framework import generics

class BlogView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer