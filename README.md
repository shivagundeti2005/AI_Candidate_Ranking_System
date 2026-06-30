 🚀 AI Candidate Ranking System

An AI-powered recruitment platform that automates candidate screening by analyzing resumes, matching them with job descriptions, and ranking applicants based on semantic similarity, skills, and experience.

 📌 Project Overview

Recruiters often spend hours manually reviewing resumes. This project uses Natural Language Processing (NLP) and AI to automate candidate evaluation and identify the most suitable applicants for a job.

The system accepts a Job Description and a candidate dataset, performs AI-based matching, and generates a ranked list of candidates with match scores and explanations.

---

 ✨ Features

- 📄 Upload Job Description (.txt or .docx)
- 👤 Upload Candidate Dataset (.jsonl)
- 📑 Resume PDF Upload (Optional)
- 🤖 AI Semantic Matching using Sentence Transformers
- 📊 Candidate Ranking Dashboard
- 🏆 Leaderboard with Rank & Score
- 📈 Interactive Charts
- 💡 AI Match Explanation
- 📥 Download Ranked Results as CSV
- 🌐 Streamlit Web Application

---

 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| Sentence Transformers | Semantic Similarity |
| PyTorch | AI Model |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| PyMuPDF | Resume PDF Parsing |
| python-docx | Read DOCX Job Descriptions |

---

📂 Project Structure

```text
AI_Candidate_Ranking_System/
│
├── app.py                  # Streamlit Web Application
├── ranking.py              # AI Ranking Engine
├── requirements.txt        # Python Dependencies
├── README.md
├── .gitignore
│
├── dataset/
│   ├── candidates_sample.jsonl
│   ├── job_description.docx
│   └── sample_submission.csv
│
└── screenshots/
```

---

 ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shivagundeti2005/AI_Candidate_Ranking_System.git
```

Move into the project directory

```bash
cd AI_Candidate_Ranking_System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

🚀 How It Works

### Step 1
Upload the Job Description.

### Step 2
Upload the Candidate Dataset.

### Step 3
(Optional) Upload a Resume PDF.

### Step 4
The AI model analyzes:

- Skills
- Experience
- Semantic Similarity
- Job Relevance

### Step 5
Candidates are ranked based on the calculated AI score.

### Step 6
View the dashboard and download the ranked results.

---

## 📊 AI Ranking Workflow

```text
Job Description
        │
        ▼
Sentence Transformer Embedding
        │
        ▼
Candidate Profile Embedding
        │
        ▼
Semantic Similarity
        │
        ▼
Skill Matching
        │
        ▼
Experience Evaluation
        │
        ▼
Final Weighted Score
        │
        ▼
Candidate Ranking
```

---

 📸 Dashboard Preview

Add screenshots here after deployment.

```
screenshots/login.png: ![Alt text](https://github.com/shivagundeti2005/AI_Candidate_Ranking_System/blob/main/Assests/login%20.png)
screenshots/dashboard.png : https://github.com/shivagundeti2005/AI_Candidate_Ranking_System/blob/main/Assests/dashboard.png
screenshots/leaderboard.png : https://github.com/shivagundeti2005/AI_Candidate_Ranking_System/blob/main/Assests/leaderboard.png
screenshots/charts.png : https://github.com/shivagundeti2005/AI_Candidate_Ranking_System/blob/main/Assests/charts.png
```

---

## 📈 Future Improvements

- Google Login
- Resume Parsing with OCR
- GPT-powered Candidate Explanation
- Skill Gap Analysis
- Multi-Job Matching
- HR Analytics Dashboard
- Email Notifications
- Interview Recommendation System

---

## 🎯 Use Cases

- Recruitment Agencies
- HR Teams
- Campus Hiring
- Talent Acquisition
- AI Recruitment Platforms
- Resume Screening Automation

---

## 📚 AI Model

The project uses the following embedding model:

```
sentence-transformers/all-MiniLM-L6-v2
```

This model converts both job descriptions and candidate profiles into embeddings and computes semantic similarity for intelligent candidate ranking.

---

## 📦 Requirements

```
streamlit
torch
sentence-transformers
python-docx
PyMuPDF
pandas
numpy
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

*👨‍💻 Shiva Gundeti

📧 Email: shivakumargundeti5@gmail.com
📱 Phone: +91 6302667395
💻 GitHub: https://github.com/shivagundeti2005
🔗 LinkedIn: https://www.linkedin.com/in/shivakumar-gundeti-164428313/
---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

💬 Share your feedback

---

## 📧 Contact

For suggestions, collaborations, or project discussions:

GitHub:
https://github.com/shivagundeti2005

Email:
shivakumargundeti5@gmail.com

---

# 🌟 AI Candidate Ranking System

### Smart Resume Screening • AI Candidate Matching • Intelligent Recruitment • Streamlit Dashboard
