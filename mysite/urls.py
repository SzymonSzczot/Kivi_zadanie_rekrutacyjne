from django.contrib import admin
from django.urls import include, path

from API.views import register, login_user

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register', register),
    path('login', login_user),
    path('main/', include('API.urls'))
]
