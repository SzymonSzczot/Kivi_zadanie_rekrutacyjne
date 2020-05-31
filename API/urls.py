from django.urls import path

from .views import (
	init_database,
	users_list,
	courses_list,
	posts_list,
	page_list,
	filter_courses_by_level)

urlpatterns = [
	path('add_test_data', init_database),
	path('users', users_list),
	path('courses', courses_list),
	path('posts', posts_list),
	path('all', page_list),
	path('all/<int:level>', filter_courses_by_level),
]
