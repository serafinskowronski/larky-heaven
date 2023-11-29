from django.urls import path
from . import views

urlpatterns = [
    path('submit_course_group/', views.submit_course_group, name='submit_course_group'),
    path('get_course_groups/', views.get_course_groups, name='get_course_groups'),
]