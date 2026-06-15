import streamlit as st

st.set_page_config(page_title="Projects | Rechal Johanna", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .proj-card {
        background: #1A1A2E;
        border: 1px solid #2D2D44;
        border-radius: 12px;
        padding: 1.4rem;
        margin-bottom: 1.2rem;
        transition: border-color 0.3s;
    }
    .proj-card:hover { border-color: #7F77DD; }
    .proj-title { font-size: 1.15rem; font-weight: 700; color: #FFFFFF; }
    .proj-type  { font-size: 0.78rem; color: #5DCAA5; font-weight: 600;
                  background: #0F2A22; border-radius: 20px; padding: 2px 10px;
                  display: inline-block; margin-bottom: 0.5rem; }
    .proj-desc  { font-size: 0.9rem; color: #C5CDD9; line-height: 1.6; }
    .tag        { display: inline-block; background: #2D2D44; color: #7F77DD;
                  border-radius: 4px; padding: 2px 8px; font-size: 0.78rem; margin: 2px; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Projects & Experience")
st.markdown("---")

# ---------- INTERNSHIPS ----------
st.markdown("## 💼 Internship Experience")

st.markdown("""
<div class="proj-card">
    <div class="proj-type">Internship — Aug 2025 to Nov 2025</div>
    <div class="proj-title">Detection of Vegetables Using OpenCV Python — Intern Certify</div>
    <div class="proj-desc">
        Built a real-time vegetable detection system using <strong>OpenCV</strong> and Python.
        Collected, processed, and analyzed image datasets for model training and validation.
        Applied analytical thinking to evaluate model accuracy and improve detection results.
        Documented project methodology and all technical findings.
        <br><br>
        <strong>Key outcomes:</strong> Improved detection accuracy through iterative model evaluation;
        produced full technical documentation for handover.
    </div>
    <br>
    <span class="tag">Python</span>
    <span class="tag">OpenCV</span>
    <span class="tag">Image Processing</span>
    <span class="tag">Data Analysis</span>
    <span class="tag">Model Validation</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="proj-card">
    <div class="proj-type">Job Simulation — March 2026</div>
    <div class="proj-title">Data Analytics Job Simulation — Deloitte Australia (Forage)</div>
    <div class="proj-desc">
        Completed Deloitte's official job simulation involving <strong>data analysis and forensic technology</strong>.
        Created a professional data dashboard using <strong>Tableau</strong> to communicate business insights.
        Used <strong>Excel</strong> to classify data, build pivot analysis, and draw meaningful business conclusions.
        <br><br>
        <strong>Key outcomes:</strong> Produced a client-ready Tableau dashboard;
        demonstrated business analyst skills in a real consulting context.
    </div>
    <br>
    <span class="tag">Tableau</span>
    <span class="tag">Excel</span>
    <span class="tag">Data Analytics</span>
    <span class="tag">Forensic Technology</span>
    <span class="tag">Dashboard Design</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- ACADEMIC PROJECTS ----------
st.markdown("## 🎓 Academic Projects")
st.caption("Add your college projects below — edit the code to fill in your actual details.")

projects = [
    {
        "title": "📌 Your Academic Project 1",
        "type": "Academic Project — Year",
        "desc": "Describe what you built, what problem it solved, the dataset or tools used, and the result. e.g. 'Built a sales forecasting model using Python/Pandas achieving 92% accuracy on test data.'",
        "tags": ["Python", "Pandas", "Matplotlib", "SQL"],
        "link": ""
    },
    {
        "title": "📌 Your Academic Project 2",
        "type": "Academic Project — Year",
        "desc": "Describe what you built. Tip: use the format → Problem → Approach → Result. Numbers make it stronger: 'Reduced processing time by 30%', 'Analyzed 10,000 records'.",
        "tags": ["Power BI", "Excel", "Data Analysis"],
        "link": ""
    },
    {
        "title": "📌 Your Academic Project 3 (AI/ML)",
        "type": "AI / ML Project — Year",
        "desc": "If you have any Gen AI, ML, or NLP project add it here. This is your biggest differentiator as a fresh graduate. Even a small working model counts.",
        "tags": ["Python", "Scikit-learn", "Gen AI", "ML"],
        "link": ""
    },
]

for proj in projects:
    with st.container():
        st.markdown(f"""
        <div class="proj-card">
            <div class="proj-type">{proj['type']}</div>
            <div class="proj-title">{proj['title']}</div>
            <div class="proj-desc">{proj['desc']}</div>
            <br>
            {''.join(f'<span class="tag">{t}</span>' for t in proj['tags'])}
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.info("💡 **Tip for recruiters:** Replace the placeholder projects above with your real college projects. Each one should follow: Problem → What you did → Tools used → Result/Impact.")

# ---------- ADD PROJECT FORM ----------
st.markdown("### ➕ Add a New Project")
with st.expander("Click to add a project"):
    c1, c2 = st.columns(2)
    with c1:
        p_title = st.text_input("Project Title")
        p_type  = st.selectbox("Type", ["Academic", "Internship", "Personal", "Freelance"])
        p_year  = st.text_input("Year / Duration")
    with c2:
        p_tools = st.text_input("Tools Used (comma separated)")
        p_link  = st.text_input("GitHub / Demo Link (optional)")
    p_desc = st.text_area("Project Description", height=100)
    if st.button("Preview Entry"):
        st.success(f"**{p_title}** ({p_type}, {p_year})\n\n{p_desc}\n\nTools: {p_tools}")
        st.caption("Copy this info into the `projects` list in the code to make it permanent.")
