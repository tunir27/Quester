from django.urls import path
from . import views

urlpatterns = [
    path('train/',views.QuesterTrainView,name='Train View'),
    path('exam/',views.QuesterExamView,name='Exam View'),
    path('validate/',views.ValidatorView,name='Validator View'),
    path('blank/',views.MLView,name='ML View'),


]
