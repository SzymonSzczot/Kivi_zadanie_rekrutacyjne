# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render

from .models import (
	User,
	Post,
	Course
)
from .serializers import (
	UserSerializer,
	CourseSerializer,
	PostSerializer
)


def init_database(request):
	Post.objects.all().delete()
	User.objects.all().delete()
	Course.objects.all().delete()

	User.objects.create(first_name="Imię", last_name="Nazwisko",
	                    prof_pic="https://www.pk.edu.pl/images/news/2019/03/KF.jpg")
	User.objects.create(first_name="Imię2", last_name="Nazwisko2",
	                    prof_pic="https://www.pk.edu.pl/images/news/2019/03/KF.jpg")

	Course.objects.create(name="Test", level=1, time_needed=200, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)
	Course.objects.create(name="Test2", level=2, time_needed=100, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)
	Course.objects.create(name="Test3", level=0, time_needed=100, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)

	user = User.objects.filter(first_name="Imię")[0]
	course = Course.objects.filter(name="Test")[0]
	Post.objects.create(User=user, Course=course, body="Opinia o kursie", stars=10)

	posts = Post.objects.all()
	users = User.objects.all()
	courses = Course.objects.all()

	template_name = 'front/base.html'
	context = {'posts': posts, 'users': users, 'courses': courses}
	return render(request, template_name, context)


def users_list(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return JsonResponse(serializer.data, safe=False)


def courses_list(request):
	if request.method == 'GET':
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return JsonResponse(serializer.data, safe=False)


def posts_list(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JsonResponse(serializer.data, safe=False)


def page_list(request):
	if request.method == 'GET':
		users = User.objects.all()
		posts = Post.objects.all()
		courses = Course.objects.all()

		serializer1 = PostSerializer(posts, many=True)
		serializer2 = CourseSerializer(courses, many=True)
		serializer3 = UserSerializer(users, many=True)
		return JsonResponse(serializer1.data + serializer2.data + serializer3.data, safe=False)


def filter_courses_by_level(request, level):
	if request.method == 'GET':
		# users = User.objects.all()
		posts = Post.objects.all()
		courses = Course.objects.filter(level=level)

		serializer1 = PostSerializer(posts, many=True)
		serializer2 = CourseSerializer(courses, many=True)
		# serializer3 = UserSerializer(users, many=True)
		return JsonResponse(serializer1.data + serializer2.data,
		                    # + serializer3.data,
		                    safe=False)
