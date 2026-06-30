import streamlit as st
import json
import pandas as pd
import fitz  # PDF reader
from docx import Document
from ranking import rank_candidates

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Hiring OS", layout="wide")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ================= LOGIN PAGE =================
def login():
    st.title("🚀 AI Hiring OS Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email and password:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Enter credentials")


# ================= PDF EXTRACT =================
def extract_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# ================= DASHBOARD =================
def dashboard():

    st.title("🚀 AI Candidate Ranking System")

    # ---------------- UPLOAD ----------------
    job_file = st.sidebar.file_uploader("📄 Job Description", type=["txt", "docx"])
    cand_file = st.sidebar.file_uploader("👤 Candidates (.jsonl)", type=["jsonl"])
    resume_file = st.sidebar.file_uploader("📎 Resume PDF", type=["pdf"])

    run = st.sidebar.button("🚀 Run AI Ranking")

    # ---------------- READ JOB ----------------
    def read_job(file):
        if file.name.endswith(".docx"):
            doc = Document(file)
            return " ".join([p.text for p in doc.paragraphs])
        return file.read().decode("utf-8")

    # ---------------- RUN ----------------
    if run:

        if job_file is None or cand_file is None:
            st.error("Upload files")
            st.stop()

        job_text = read_job(job_file)

        resume_text = ""
        if resume_file:
            resume_text = extract_pdf(resume_file)
            st.subheader("📄 Resume Preview")
            st.write(resume_text[:800])

        # ---------------- CANDIDATES ----------------
        candidates = []
        for line in cand_file:
            try:
                candidates.append(json.loads(line))
            except:
                continue

        # ---------------- AI RANKING ----------------
        results = rank_candidates(job_text, candidates)

        for i, r in enumerate(results, start=1):
            r["rank"] = i

        df = pd.DataFrame(results)

        st.success("🏆 Ranking Completed")

        # ---------------- KPI DASHBOARD ----------------
        col1, col2, col3 = st.columns(3)

        col1.metric("👥 Candidates", len(df))
        col2.metric("🏆 Top Score", round(df["score"].max(), 2))
        col3.metric("📊 Avg Score", round(df["score"].mean(), 2))

        st.divider()

        # ---------------- LEADERBOARD ----------------
        st.subheader("🏆 Leaderboard")
        st.dataframe(df, use_container_width=True)

        # ---------------- GRAPH ----------------
        st.subheader("📊 Ranking Chart")
        st.bar_chart(df.head(10).set_index("candidate_id")[["score"]])

        # ---------------- SKILL ANALYSIS (PIE STYLE) ----------------
        st.subheader("🥧 Skill Distribution")

        skill_counts = df["candidate_id"].value_counts().head(5)
        st.bar_chart(skill_counts)

        # ---------------- AI EXPLANATION PANEL ----------------
        st.subheader("🤖 AI Explanation Panel")

        for r in results[:5]:
            with st.expander(f"Candidate {r['candidate_id']}"):

                st.write("🏆 Score:", r["score"])

                st.write("🧠 Why Selected:")
                st.info(r.get("reason", "Strong semantic + skill match"))

        # ---------------- DOWNLOAD ----------------
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button("📥 Download Report", csv, "ranking.csv", "text/csv")


# ================= ROUTER =================
if not st.session_state.logged_in:
    login()
else:
    dashboard()