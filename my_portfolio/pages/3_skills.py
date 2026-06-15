import streamlit as st

st.set_page_config(page_title="Skills | Rechal Johanna Ramakuri", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
    .skill-label { font-size: 0.95rem; font-weight: 600; color: #E2E8F0; margin: 0.8rem 0 0.2rem; }
    .skill-sub   { font-size: 0.8rem;  color: #64748B; margin-bottom: 0.3rem; }
    .cat-header  { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em;
                   text-transform: uppercase; color: #A78BFA; margin: 1.2rem 0 0.6rem;
                   border-bottom: 1px solid #1E293B; padding-bottom: 4px; }
    .tool-badge  { display: inline-block; background: #0F172A; color: #34D399;
                   border: 1px solid #065F46; border-radius: 20px;
                   padding: 5px 14px; font-size: 0.82rem; margin: 4px; }
    .learning-badge { display: inline-block; background: #1C1917; color: #FBBF24;
                   border: 1px solid #92400E; border-radius: 20px;
                   padding: 5px 14px; font-size: 0.82rem; margin: 4px; }
</style>
""", unsafe_allow_html=True)

st.title("🛠️ Skills & Tech Stack")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="cat-header">🐍 Core Data Science Stack</div>', unsafe_allow_html=True)

    for skill, sub in [
        ("Python",          "Pandas, NumPy, OpenCV, Scikit-learn"),
        ("SQL / MySQL",     "Complex queries, joins, subqueries, DB design"),
        ("Data Analysis",   "EDA, pattern recognition, 500+ records analyzed"),
        ("MS Excel",        "Pivot tables, VLOOKUP, statistical analysis"),
    ]:
        st.markdown(f'<div class="skill-label">{skill} </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="skill-sub">{sub}</div>', unsafe_allow_html=True)

    st.markdown('<div class="cat-header">🧠 AI / Gen AI</div>', unsafe_allow_html=True)

    for skill, sub in [
        ("Groq API / LLM Integration",       "Built real Gen AI apps with Groq API"),
        ("Prompt Engineering",              "Designed prompts for LLM-based outputs"),
        ("OpenCV / Computer Vision",        "Image datasets, model validation (internship)"),
    ]:
        st.markdown(f'<div class="skill-label">{skill} </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="skill-sub">{sub}</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="cat-header">📊 BI & Visualization</div>', unsafe_allow_html=True)

    for skill, sub in [
        ("Power BI",     "Dashboards, DAX, data modeling"),
        ("Tableau",      "Built dashboards for Deloitte simulation"),
        ("Streamlit",    "Full app UI — used in Gen AI internship project"),
        ("Matplotlib / Seaborn",  "Statistical plots, EDA visualizations"),
    ]:
        st.markdown(f'<div class="skill-label">{skill} </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="skill-sub">{sub}</div>', unsafe_allow_html=True)

    st.markdown('<div class="cat-header">⚙️ Dev & Workflow Tools</div>', unsafe_allow_html=True)

    for skill, sub in [
        ("GitHub / Version Control",  "Repos, commits, project management"),
        ("VS Code",                   "Primary IDE for all projects"),
        ("Jupyter Notebook",          "Data exploration, ML experiments"),
        ("M365 PowerApps",            "App automation, Microsoft ecosystem"),
    ]:
        st.markdown(f'<div class="skill-label">{skill} </div>', unsafe_allow_html=True)
        st.markdown(f'<div class="skill-sub">{sub}</div>', unsafe_allow_html=True)

st.markdown("---")

# ── Concepts ──────────────────────────────────────────────────────────
st.markdown("### 📚 Data Science Concepts")
concepts = [
    "Supervised Learning", "Classification & Regression",
    "Model Evaluation & Validation", "Feature Engineering",
    "EDA & Statistical Analysis", "Data Cleaning & Wrangling",
    "Database Management", "Computer Vision",
    "LLM Integration", "Business Intelligence",
    "Research Methodology", "OOP in Python",
]
cols = st.columns(4)
for i, c in enumerate(concepts):
    with cols[i % 4]:
        st.markdown(f'<span class="tool-badge">{c}</span>', unsafe_allow_html=True)

st.markdown("---")

# ── Currently Learning ────────────────────────────────────────────────
st.markdown("### 🚀 Currently Levelling Up")
learning = ["Deep Learning (TensorFlow/Keras)", "LangChain & RAG Pipelines",
            "MLflow / Model Deployment", "Docker for ML", "AWS / Cloud Basics",
            "Advanced Scikit-learn Pipelines"]
for item in learning:
    st.markdown(f'<span class="learning-badge">⚡ {item}</span>', unsafe_allow_html=True)

st.markdown("---")
