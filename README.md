# Resume-Analyzer
# 🧠 Resume Analyzer (Django + Machine Learning)

A web-based **Resume Analyzer** built with **Django** that uses a **Machine Learning model** to automatically analyze resumes and provide insights such as:

- Predicted job/domain category  
- Matching score against a given job description  
- Highlighted missing skills / keywords  
- Recommendations to improve the resume  

> This project can be extended into a full recruitment helper for HR teams or students preparing for placements.

---

## 🚀 Features

- Upload resumes in **PDF / DOCX / TXT** formats  
- Extracts text using NLP-based preprocessing  
- Classifies resumes into **predefined categories** (e.g., Data Science, Web Dev, ML Engineer, etc.)  
- Computes **similarity score** with a job description (optional)  
- Displays **skills, experience, and key sections** detected from the resume  
- REST-style **API endpoint** for programmatic access  
- Admin panel to view analysis history and manage users (Django Admin)

---

## 🧰 Tech Stack

- **Backend Framework**: Django (Python)
- **ML / NLP**: scikit-learn / spaCy / NLTK (depending on your implementation)
- **Model Types** (example):
  - TF-IDF Vectorizer
  - Logistic Regression / SVM / Random Forest (for classification)
  - Cosine Similarity (for job-resume matching)
- **Database**: SQLite (default) / PostgreSQL (for production)
- **Frontend**: Django Templates / HTML / CSS / Bootstrap
