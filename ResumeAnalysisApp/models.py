# ResumeAnalysisApp/models.py
from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.username

class Feedback(models.Model):
    username = models.CharField(max_length=100)
    feedback = models.TextField()
    feedback_date = models.DateField(auto_now_add=True)
    feedback_rank = models.IntegerField()

    def __str__(self):
        return f"{self.username} - {self.feedback_date}"

class JobPost(models.Model):
    job_name = models.CharField(max_length=100)
    job_details = models.TextField()
    skills = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.job_name

class ResumeUpload(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    resume_name = models.CharField(max_length=100)
    upload_date = models.DateField(auto_now_add=True)
    resume_json = models.TextField()
    resume_score = models.IntegerField()

    def __str__(self):
        return f"{self.username} - {self.job.job_name}"

