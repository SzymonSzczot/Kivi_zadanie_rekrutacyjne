from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    prof_pic = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


LEVELS = [
    (0, 'zaaawansowany'),
    (1, 'średnio-zaawansowany'),
    (2, 'poczatkujacy')]


class Course(models.Model):
    name = models.CharField(max_length=128)
    level = models.CharField(choices=LEVELS, default='unassigned', max_length=100)
    time_needed = models.PositiveIntegerField()
    price = models.FloatField()

    is_free = models.BooleanField()
    is_shared = models.BooleanField()
    mind_master = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OwnedCourses(models.Model):
    User = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="user")
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="course")
    price = models.PositiveIntegerField()
    progress = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    User = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="user")
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="course")
    stars = models.PositiveIntegerField()
    body = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)