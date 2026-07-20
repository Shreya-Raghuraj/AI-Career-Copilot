# AI Career Co-Pilot

An AI-powered career assistant that helps users analyze resumes, identify skill gaps, discover suitable job roles, and receive personalized career guidance using Google Gemini AI.

---

## ✨ Features

- 📄 Resume Upload & Parsing
- 📊 ATS Resume Score Analysis
- 🤖 AI-Powered Resume Feedback
- 💼 Best Job Role Recommendation
- 🧠 Skill Gap Analysis
- 🗺️ Personalized Learning Roadmap
- 💬 AI Career Chatbot
- 🎨 Modern Responsive UI with Tailwind CSS & Framer Motion

---

## 📸 Screenshots

> *(Add screenshots of your application here)*

### 🏠 Home Page
![Home](screenshots/home.png)

### 📊 Dashboard
![Dashboard](screenshots/dashboard.png)

### 💬 AI Chatbot
![Chatbot](screenshots/chatbot.png)

### 📄 Resume Upload
![Resume](screenshots/resume.png)

---

# 🛠 Tech Stack

## Frontend
- React.js
- Vite
- Tailwind CSS
- Framer Motion
- Axios
- React Router DOM

## Backend
- FastAPI
- Python
- Uvicorn

## AI & LLM
- Google Gemini API
- Groq API
- LangChain
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering

## Vector Database
- ChromaDB

## Data Processing
- PyPDF
- Pandas
- NumPy

## Version Control & Tools
- Git
- GitHub
- VS Code
---
## ✨ Features

- 📄 Resume Upload & Parsing
- 📊 AI-powered ATS Resume Score
- 🤖 Personalized Resume Feedback
- 💼 Best Job Role Recommendation
- 🧠 Skill Gap Analysis
- 🗺️ Personalized Learning Roadmap
- 💬 AI Career Chatbot powered by LangChain + Groq
- 🔍 RAG-based document retrieval using ChromaDB
- ⚡ FastAPI REST APIs
- 🎨 Responsive UI built with React & Tailwind CSS

# 📂 Project Structure

```
AI-Career-CoPilot
│
├── backend
│   ├── main.py
│   ├── chat.py
│   ├── resume_parser.py
│   ├── roadmap.py
│   └── ...
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── ...
│
├── requirements.txt
└── README.md
```

---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/Shreya-Raghuraj/AI-Career-CoPilot.git
```

---

## Backend Setup

```bash
cd backend

pip install -r ../requirements.txt

uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# Workflow

1. Upload your resume.
2. Resume is parsed using the backend.
3. Google Gemini analyzes the resume.
4. ATS score is generated.
5. Skills are extracted.
6. Best matching job role is predicted.
7. AI provides personalized career guidance.
8. Users can interact with the Career Chatbot for additional support.

---

# 🌟 Future Improvements

- User Authentication
- Resume History
- Interview Preparation Module
- Resume Builder
- Job Recommendation API
- Resume Comparison
- Dark/Light Theme Toggle
- Deployment on Render/Vercel

---

# 👩‍💻 Author

**Shreya Raghuraj**

AI & Machine Learning Engineering Student passionate about building AI-powered applications that solve real-world problems.

---

## ⭐ If you found this project interesting, consider giving it a star!
