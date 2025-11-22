# ResumeAnalysisApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('post_jobs/', views.post_jobs, name='post_jobs'),
    path('feedback/', views.feedback, name='feedback'),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('view_jobs/', views.view_jobs, name='view_jobs'),
    path('view_score/', views.view_score, name='view_score'),
    path('logout/', views.logout_view, name='logout'),
]

