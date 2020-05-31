# coding=utf-8
import django
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest

from .models import (
	MyUser,
	Post,
	Course,
	OwnedCourses
)
from .serializers import (
	UserSerializer,
	CourseSerializer,
	PostSerializer
)

@csrf_exempt
def register(request):
	username = request.POST['login']
	password = request.POST['password']

	try:
		MyUser.objects.create_user(first_name="first_name", last_name="last_name", prof_pic="pic",
		                    username=username, password=password)
	except django.db.utils.IntegrityError:
		response = JsonResponse({"MyUser": "Already exists"})
		response.status_code = 403

@csrf_exempt
def login_user(request):
	username = request.POST['login']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		response = JsonResponse({"MyUser": "Im in"})
		response.status_code = 200
	else:
		response = JsonResponse({"MyUser": "Invalid login"})
		response.status_code = 403


def init_database(request):
	Post.objects.all().delete()
	# MyUser.objects.all().delete()
	# Course.objects.all().delete()

	MyUser.objects.create(first_name="Imię", last_name="Nazwisko",
	                    prof_pic="https://www.pk.edu.pl/images/news/2019/03/KF.jpg",
	                    username="test1", password="admin")
	MyUser.objects.create(first_name="Imię2", last_name="Nazwisko2",
	                    prof_pic="https://www.pk.edu.pl/images/news/2019/03/KF.jpg",
	                    username="test2", password="admin")

	Course.objects.create(name="Test3", level=0, time_needed=100, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)

	MyUser.objects.create_user(first_name="MyUser", last_name="testowy", prof_pic="link_to_jpg",
	                    username="username", password="admin123")

	c1 = Course.objects.create(name="Test", level=1, time_needed=200, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)
	c2 = Course.objects.create(name="Test2", level=2, time_needed=100, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)
	c3 = Course.objects.create(name="Test4", level=1, time_needed=100, price=39.54, is_free=False, is_shared=True,
	                      mind_master=False)

	showed_user = MyUser.objects.get(username="username")

	OwnedCourses.objects.create(MyUser=showed_user, Course=c1, price=10.0, progress=0)
	OwnedCourses.objects.create(MyUser=showed_user, Course=c2, price=15.0, progress=50)
	OwnedCourses.objects.create(MyUser=showed_user, Course=c3, price=0.0, progress=100)

	course = Course.objects.filter(name="Test")[0]

	Post.objects.create(MyUser=showed_user, Course=course, body="Opinia o kursie", stars=10)

	log_user = authenticate(request, username="username", password="admin123")

	print(log_user)

	if log_user is not None:
		login(request, log_user)

	print(request.user.is_authenticated)
	print(request.user.get_username())

	posts = Post.objects.all()
	users = MyUser.objects.all()
	courses = Course.objects.all()

	template_name = 'front/base.html'
	context = {'posts': posts, 'users': users, 'courses': courses}
	return render(request, template_name, context)


def users_list(request):
	if request.method == 'GET':
		users = MyUser.objects.all()
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
		users = MyUser.objects.all()
		posts = Post.objects.all()

		print(OwnedCourses.objects.all())

		crs_list = []

		for c in OwnedCourses.objects.all():
			crs_list.append(c.Course.name)

		courses = Course.objects.filter(name__in=crs_list)

		serializer1 = PostSerializer(posts, many=True)
		serializer2 = CourseSerializer(courses, many=True)
		serializer3 = UserSerializer(users, many=True)
		return JsonResponse(serializer1.data
		                    + serializer2.data
		                    # + serializer3.data
		                    , safe=False)


def filter_courses_by_level(request, level):
	if request.method == 'GET':
		usr = request.user.is_authenticated
		print(request.user.get_username)
		posts = Post.objects.all()
		courses = Course.objects.filter(level=level)

		serializer1 = PostSerializer(posts, many=True)
		serializer2 = CourseSerializer(courses, many=True)
		# serializer3 = MyUserSerializer(users, many=True)
		return JsonResponse(serializer1.data + serializer2.data,
		                    # + serializer3.data,
		                    safe=False)
