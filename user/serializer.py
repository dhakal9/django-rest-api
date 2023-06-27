from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blogs, User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        


class LoginSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        return representation
        
    
class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ['url', 'name']

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blogs
        fields = ['title', 'discription','img']
        
# class UpdateBlogSerializer(serializers.ModelSerializer):
    
#     title = serializers.CharField(max_len)
#     class Meta:
#         model = Blogs
#         fields = ['title', 'discription']
