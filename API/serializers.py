from rest_framework import serializers

from .models import MyUser, Course, Post


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'level', 'time_needed', 'price', 'is_free', 'is_shared', 'mind_master']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['MyUser', 'Course', 'body', 'stars']
