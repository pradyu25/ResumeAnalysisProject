# ResumeAnalysisApp/admin.py
from django.contrib import admin
from .models import Signup, Feedback, JobPost, ResumeUpload

admin.site.register(Signup)
admin.site.register(Feedback)
admin.site.register(JobPost)
admin.site.register(ResumeUpload)

