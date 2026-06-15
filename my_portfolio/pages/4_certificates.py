import streamlit as st
from datetime import date

st.set_page_config(page_title="Certificates | Rechal Johanna", page_icon="🏅", layout="wide")

st.markdown("""
<style>
    .cert-card {
        background: #1A1A2E;
        border: 1px solid #2D2D44;
        border-radius: 12px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
    }
    .cert-title  { font-size: 1.05rem; font-weight: 700; color: #FFFFFF; }
    .cert-issuer { font-size: 0.9rem;  color: #7F77DD; margin: 0.2rem 0; }
    .cert-date   { font-size: 0.82rem; color: #9FA6B2; }
    .cert-badge  {
        display: inline-block; background: #0F2A22; color: #5DCAA5;
        border-radius: 20px; padding: 3px 12px; font-size: 0.78rem;
        margin-bottom: 0.6rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏅 Certifications & Achievements")
st.markdown("---")

st.markdown("## ✅ Earned Certifications")

certs = [
    {
        "title": "Data Analytics Job Simulation",
        "issuer": "Deloitte Australia via Forage",
        "date": "March 2026",
        "badge": "Industry Simulation",
        "skills": "Data Analysis, Tableau, Excel, Forensic Technology",
        "desc": "Completed Deloitte's official virtual job simulation. Built a Tableau dashboard and used Excel to classify data and draw business conclusions in a forensic analytics context.",
        "link": "https://www.theforage.com"
    },
    {
        "title": "SQL Certificate",
        "issuer": "Simplilearn",
        "date": "2025",
        "badge": "Technical Certification",
        "skills": "SQL queries, joins, subqueries, database design",
        "desc": "Earned industry-recognized SQL certification covering database management, complex queries, and data manipulation using MySQL.",
        "link": "https://www.simplilearn.com"
    },
]

for cert in certs:
    st.markdown(f"""
    <div class="cert-card">
        <div class="cert-badge">{cert['badge']}</div>
        <div class="cert-title">{cert['title']}</div>
        <div class="cert-issuer">🏢 {cert['issuer']}</div>
        <div class="cert-date">📅 {cert['date']} &nbsp;|&nbsp; 🛠 {cert['skills']}</div>
        <p style="font-size:0.88rem; color:#C5CDD9; margin-top:0.6rem;">{cert['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Placeholder for more certs ---
st.markdown("## 📌 Add More Certifications")
st.caption("Replace the placeholder cards below with your actual certificates — Google, Microsoft, AWS, Coursera, NPTEL etc.")

placeholder_certs = [
    {"title": "Your Certification Title", "issuer": "Issuer Name (e.g. Google, Coursera, NPTEL)", "date": "Month Year", "badge": "Add your cert type"},
    {"title": "Your Certification Title", "issuer": "Issuer Name", "date": "Month Year", "badge": "Add your cert type"},
]

for cert in placeholder_certs:
    st.markdown(f"""
    <div class="cert-card" style="border: 1px dashed #4A4A6A; opacity: 0.7;">
        <div class="cert-badge" style="background:#2D2D44; color:#9FA6B2;">{cert['badge']}</div>
        <div class="cert-title" style="color:#9FA6B2;">{cert['title']}</div>
        <div class="cert-issuer">{cert['issuer']}</div>
        <div class="cert-date">📅 {cert['date']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Upload certificate images ---
st.markdown("## 📎 Upload Certificate Images")
st.caption("Upload your certificate images to display them visually on your portfolio.")

uploaded = st.file_uploader(
    "Upload certificate images (JPG, PNG, PDF)",
    type=["jpg", "jpeg", "png", "pdf"],
    accept_multiple_files=True
)

if uploaded:
    cols = st.columns(min(len(uploaded), 3))
    for i, f in enumerate(uploaded):
        with cols[i % 3]:
            if f.type in ["image/jpeg", "image/png"]:
                st.image(f, caption=f.name, use_column_width=True)
            else:
                st.markdown(f"📄 **{f.name}** (PDF — view after download)")

st.markdown("---")
st.info("💡 **Recruiter tip:** Aim to earn 1-2 new certifications per quarter. Great next steps: Google Data Analytics (Coursera), Microsoft Power BI Certification, or AWS Cloud Practitioner.")
