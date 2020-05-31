from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager


class MyUser(User):
    prof_pic = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


LEVELS = [
    (0, 'zaaawansowany'),
    (1, 'średnio-zaawansowany'),
    (2, 'poczatkujacy')]


class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)
    level = models.CharField(choices=LEVELS, default='unassigned', max_length=100)
    time_needed = models.PositiveIntegerField()
    price = models.FloatField()

    is_free = models.BooleanField()
    is_shared = models.BooleanField()
    mind_master = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OwnedCourses(models.Model):
    MyUser = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name="user")
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="course")
    price = models.PositiveIntegerField()
    progress = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    MyUser = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, verbose_name="user")
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="course")
    stars = models.PositiveIntegerField()
    body = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)