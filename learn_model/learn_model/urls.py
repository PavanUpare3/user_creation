
from django.contrib import admin
from django.urls import path, include
from first_model_file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display),
    path('', include('learn_signup.urls'))
]
