import streamlit as st

st.set_page_config(page_title="About | Rechal Johanna Ramakuri", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>
    .edu-card {
        background: #0F172A; border-left: 4px solid #A78BFA;
        border-radius: 10px; padding: 1.3rem 1.6rem; margin-bottom: 1rem;
    }
    .edu-title  { font-size: 1.1rem; font-weight: 700; color: #F1F5F9; }
    .edu-inst   { font-size: 0.95rem; color: #A78BFA; margin: 0.2rem 0; }
    .edu-meta   { font-size: 0.85rem; color: #94A3B8; margin-top: 0.4rem; line-height: 1.6; }
    .highlight  { color: #34D399; font-weight: 700; }
    .value-pill {
        display: inline-block; background: #1E1B4B;
        color: #A78BFA; border: 1px solid #3730A3;
        border-radius: 8px; padding: 6px 14px;
        font-size: 0.85rem; margin: 4px; font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

st.title("👩‍💻 About Me")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### My Story")
    st.markdown("""
    I'm **Rechal Johanna Ramakuri** — a **2026 MCA graduate** from SRM Institute of Science & Technology,
    Chennai, with a **9.8 GPA** and a clear mission: to become a Data Scientist who builds AI-powered
    solutions that create real business value.

    During my postgraduate studies, I went beyond coursework to build **AI applications** using
    **Groq API, Streamlit, Python and VS Code**, managing full project lifecycles on **GitHub**.
    I also completed a real-world **Deloitte Australia Data Analytics Job Simulation** — building
    Tableau dashboards and drawing forensic business conclusions from raw data.

    My first internship involved building a **vegetable detection system using OpenCV + Python**,
    where I collected and processed image datasets, evaluated model accuracy, and documented
    technical findings end-to-end.

    I'm now ready to bring this combination of **ML fundamentals +Gen AI building skills +
    data analytics** to a high-impact Data Scientist role.
    """)

with col2:
    st.markdown("### Quick Info")
    info = {
        "🎓 Graduation": "MCA — 2026",
        "🏫 University": "SRM University, Chennai",
        "📊 GPA":        "9.8 / 10 (Upto 3rd Sem)",
        "📍 Location":   "Hyderabad, Telangana",
        "📧 Email":      "rechaljohanna@gmail.com",
        "🗣️ Languages":  "English, Telugu",
        "🎯 Target role": "Data Analyst / Data Scientist / ML Engineer",
        "🟢 Status":     "Available immediately",
    }
    for k, v in info.items():
        st.markdown(f"**{k}:** {v}")

st.markdown("---")

# ── Value Propositions ────────────────────────────────────────────────
st.markdown("### 💡 What I Bring to a Data Science Team")
values = [
    "🧠 Gen AI app development (Groq API + LLMs)",
    "📊 End-to-end data analysis pipeline",
    "🔬 Model building + validation experience",
    "📈 Business-ready dashboards (Power BI, Tableau)",
    "🐙 Clean code practices with GitHub",
    "⚡ Fast learner — 9.8 GPA proves it",
    "💬 Strong documentation & communication",
    "🏢 Industry exposure via Deloitte simulation",
]
cols = st.columns(4)
for i, v in enumerate(values):
    with cols[i % 4]:
        st.markdown(f'<div class="value-pill">{v}</div>', unsafe_allow_html=True)

st.markdown("---")

# ── Education ─────────────────────────────────────────────────────────
st.markdown("### 🎓 Education")

st.markdown("""
<div class="edu-card">
    <div class="edu-title">Master of Computer Application (M.C.A)"</div>
    <div class="edu-inst">SRM Institute of Science & Technology, Chennai</div>
    <div class="edu-meta">
        📅 2024 – 2026 &nbsp;|&nbsp; Virtual Mode &nbsp;|&nbsp;
        <span class="highlight">GPA: 9.8 / 10(Upto Sem 3)</span>
        <br><br>
        <strong>Relevant coursework:</strong> Machine Learning, Data Analytics, Deep Learning Fundamentals,
        Database Management, Research Methodology, Cloud Computing, AI Applications,
        Python for Data Science, Big Data Concepts
        <br><br>
        <strong>Key achievement:</strong> Built Gen AI applications integrating Groq API + Streamlit as part of coursework and personal projects.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="edu-card">
    <div class="edu-title">Bachelor of Computer Science (B.Sc)</div>
    <div class="edu-inst">Sir C R Reddy College For Women, Eluru</div>
    <div class="edu-meta">
        📅 2021 – 2024 &nbsp;|&nbsp;
        <span class="highlight">GPA: 8.0 / 10</span>
        <br><br>
        <strong>Relevant coursework:</strong> Data Structures, Algorithms, Database Systems (MySQL),
        Statistics, OOP with Python, Computer Networks, Operating Systems
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Awards ────────────────────────────────────────────────────────────
st.markdown("### 🏆 Awards & Achievements")
c1, c2, c3 = st.columns(3)
with c1:
    st.success("🥇 **1st Place** — Grand Talent Test\nSreedhar's Institute")
with c2:
    st.success("📊 Analyzed **500+ data records**\nfor pattern recognition & business insights")
with c3:
    st.success("🎓 **9.8 GPA** — Top performer\nMCA batch, SRM University 2026")

st.markdown("---")

# ── Interests ─────────────────────────────────────────────────────────
st.markdown("### 🌱 Beyond the Keyboard")
st.markdown("""
Outside of data and AI, I enjoy **drawing**, **cooking**, and **making crafts** — creative
pursuits that actually sharpen the same pattern recognition and design thinking I bring to my work.
I believe the best data scientists are also great storytellers, and creativity is a core part of that.
""")
