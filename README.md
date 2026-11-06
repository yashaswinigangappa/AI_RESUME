# TalentAI - AI Resume Screening & Precision Candidate Ranking Engine

A comprehensive full-stack major project that combines **Natural Language Processing (NLP)**, **TF-IDF semantic vectorization**, **ATS readiness auditing**, and **role-based portals** for Candidates, Corporate Recruiters, and Administrators.

---

## 🌟 Key Features

### 🎓 1. Candidate / Student Portal
- **AI Resume Parser**: Multi-format parsing supporting both **PDF** and **DOCX** with regex & NLP heuristics.
- **5-Dimension ATS Score**: Real-time auditing for Completeness, Action Verbs, Formatting, Quantifiable Metrics, and Skill Depth (0–100 scale).
- **Categorized Technical Taxonomy**: Automatic categorization into Programming, Frameworks, Cloud/DevOps, Databases, AI/ML, and Tools.
- **AI-Recommended Jobs**: Hybrid match score calculated using TF-IDF cosine similarity + skill overlap vectors + experience weighting.
- **Skill Gap Matrix**: Visual breakdown of matched vs. missing skills, with **curated learning resources & courses** (Coursera, Udemy, etc.) to bridge gaps.
- **Application Tracker**: Live application pipeline (Applied → Reviewing → Shortlisted → Hired / Rejected).

### 💼 2. Corporate Recruiter Portal
- **Automated Candidate Screening & Ranking**: Applicants are automatically ranked from highest to lowest by AI Match Fit.
- **Candidate Inspection**: Detailed view of candidate's parsed skills, semantic fit percentage, experience, and notes.
- **1-Click Pipeline Decisions**: Instant Shortlist, Under Review, Reject, or Extend Offer.
- **Job Creation & Management**: Publish detailed technical openings with custom required & preferred skills.
- **Recruitment Analytics**: Total jobs, screened candidates, and average candidate match quality.

### 🛡️ 3. Administrator Governance
- **Platform Analytics**: High-level platform statistics (users, students, recruiters, resumes, jobs, applications).
- **Market Demand Trends**: Visual chart of the most frequently detected technical skills across all candidate resumes.
- **User Governance**: Search users, filter by role, activate/suspend accounts, or delete users.
- **Job Moderation**: Inspect all job listings and delete expired or invalid postings.

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.10+** (tested on Python 3.14)
- **Node.js 18+** & **npm**

### 1. Launch the Backend (FastAPI)
Double-click `run_backend.bat` or run:
```bash
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
- Interactive Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Health check: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

### 2. Launch the Frontend (Vite + React)
Double-click `run_frontend.bat` or run:
```bash
cd frontend
npm run dev
```
- Open your browser to: [http://localhost:3000](http://localhost:3000)

---

## 🔑 One-Click Demo Credentials

All demo accounts use password: `password123`

| Role | Demo Email | Password | Primary Capabilities |
|---|---|---|---|
| 🎓 **Student** | `student@demo.com` | `password123` | ATS Score, AI Recommendations, Skill Gap Analysis |
| 💼 **Recruiter** | `recruiter@demo.com` | `password123` | AI Candidate Ranking, Shortlist/Reject, Post Jobs |
| 🛡️ **Admin** | `admin@demo.com` | `password123` | Platform Analytics, User Governance, Job Moderation |

*(You can also use the 1-click demo buttons right in the navigation bar to switch roles instantly!)*

---

## 🧪 Running Automated Tests

The backend includes a comprehensive test suite covering authentication, parsing, TF-IDF matching, ATS scoring, and API endpoints.

```bash
cd backend
python -m pytest
```
*Result: 19 passed.*

---

## 🏗️ Technology Stack

- **Backend**: FastAPI, Python, SQLAlchemy ORM, SQLite, Pydantic v2, PyJWT, Bcrypt
- **NLP & AI**: Scikit-Learn (TF-IDF vectorizer, cosine similarity), pypdf, python-docx
- **Frontend**: React 19, Vite, Lucide React, Glassmorphism UI, Responsive CSS Grid
