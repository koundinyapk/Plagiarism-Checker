from django.urls import path
from .views import *

urlpatterns=[
    path("",home),
    path("check_plagiarism",check_plagiarism)
]