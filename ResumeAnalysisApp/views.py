# ResumeAnalysisApp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.core.files.storage import FileSystemStorage
from datetime import date
import numpy as np
import matplotlib.pyplot as mplt
from pyresparser import ResumeParser
from .models import Signup, Feedback, JobPost, ResumeUpload


def index(request):
    return render(request, 'index.html')

def admin_login(request):
    if request.method == 'GET':
        return render(request, 'AdminLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "admin1":
            request.session['username'] = username
            return render(request, 'AdminScreen.html', {'data': 'Welcome, admin!'})
        else:
            messages.error(request, 'Invalid login details')
            return redirect('admin_login')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'UserLogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ResumeAnalysisApp_signup WHERE username = %s AND password = %s", [username, password])
            user = cursor.fetchone()
            if user:
                request.session['username'] = username
                return render(request, 'UserScreen.html', {'data': 'Welcome ' + username})
            else:
                messages.error(request, 'Invalid login details')
                return redirect('user_login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        contact = request.POST.get('t3')
        email = request.POST.get('t4')
        address = request.POST.get('t5')

        with connection.cursor() as cursor:
            cursor.execute("SELECT username FROM ResumeAnalysisApp_signup WHERE username = %s", [username])
            if cursor.fetchone():
                messages.error(request, 'Given Username already exists')
                return redirect('signup')

            cursor.execute("""
                INSERT INTO ResumeAnalysisApp_signup (username, password, contact_no, email_id, address)
                VALUES (%s, %s, %s, %s, %s)
            """, [username, password, contact, email, address])
            messages.success(request, 'Signup Process Completed')
            return redirect('signup')

    return render(request, 'Signup.html')

def post_jobs(request):
    if request.method == 'POST':
        job_name = request.POST.get('t1')
        job_details = request.POST.get('t2')
        company_name = request.POST.get('t3')
        salary = request.POST.get('t4')
        skills = ','.join(request.POST.getlist('t5'))

        JobPost.objects.create(
            job_name=job_name,
            job_details=job_details,
            skills=skills,
            company_name=company_name,
            salary=salary
        )
        messages.success(request, 'Job Posted Successfully')
        return redirect('post_jobs')

    return render(request, 'PostJobs.html')

def feedback(request):
    if request.method == 'POST':
        username = request.session.get('username', 'Anonymous')
        feedback_text = request.POST.get('t1')
        rank = int(request.POST.get('t2'))
        Feedback.objects.create(username=username, feedback=feedback_text, feedback_rank=rank)
        messages.success(request, 'Feedback submitted successfully')
        return redirect('feedback')

    return render(request, 'Feedback.html')

def upload_resume(request):
    if request.method == 'POST':
        job_id = request.POST.get('t1')
        myfile = request.FILES['t2']
        fname = request.FILES['t2'].name
        fs = FileSystemStorage()
        filename = fs.save('ResumeAnalysisApp/static/resumes/' + fname, myfile)
        data = ResumeParser('ResumeAnalysisApp/static/resumes/' + fname).get_extracted_data()
        skills = data['skills']
        score = get_score(job_id, skills)
        ResumeUpload.objects.create(
            job_id=job_id,
            username=request.session['username'],
            resume_name=fname,
            resume_json=str(data),
            resume_score=score
        )
        messages.success(request, f'Your resume submitted with score: {score}')
        return redirect('upload_resume')

    return render(request, 'UploadResume.html')

def get_score(job_id, skills):
    job = JobPost.objects.get(id=job_id)
    require_skills = job.skills.split(',')
    require_skills = [skill.strip().lower() for skill in require_skills]
    skills = [skill.lower().strip() for skill in skills]
    found_skills = [x for x in skills if x in require_skills]
    if len(found_skills) >= len(require_skills):
        score = 100
    else:
        score = (len(found_skills) / len(require_skills)) * 100
    return score

def view_feedback(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'ViewFeedback.html', context)

def view_jobs(request):
    jobs = JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request, 'ViewJobs.html', context)

def view_score(request):
    resumes = ResumeUpload.objects.all().order_by('-resume_score')
    context = {'resumes': resumes}
    return render(request, 'ViewScore.html', context)

def logout_view(request):
    return redirect('index')


