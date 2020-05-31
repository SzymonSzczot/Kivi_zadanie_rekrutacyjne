from rest_framework import serializers

from .models import User, Course, Post


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'level', 'time_needed', 'price', 'is_free', 'is_shared', 'mind_master']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['User', 'Course', 'body', 'stars']
