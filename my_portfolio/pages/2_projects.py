import streamlit as st

st.set_page_config(page_title="Projects | Rechal Johanna Ramakuri", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .proj-card {
        background: #0F172A; border: 1px solid #1E293B;
        border-radius: 14px; padding: 1.5rem; margin-bottom: 1.2rem;
        transition: border-color .2s;
    }
    .proj-card:hover { border-color: #A78BFA; }
    .proj-card-hero {
        background: linear-gradient(135deg, #1E1B4B, #0F2A22);
        border: 1.5px solid #A78BFA; border-radius: 14px;
        padding: 1.5rem; margin-bottom: 1.2rem;
    }
    .proj-type  { font-size: 0.76rem; font-weight: 700; color: #34D399;
                  background: #064E3B; border-radius: 20px;
                  padding: 3px 12px; display: inline-block; margin-bottom: 0.6rem; }
    .proj-type-blue { font-size: 0.76rem; font-weight: 700; color: #60A5FA;
                  background: #1E3A5F; border-radius: 20px;
                  padding: 3px 12px; display: inline-block; margin-bottom: 0.6rem; }
    .proj-title { font-size: 1.15rem; font-weight: 700; color: #F1F5F9; margin-bottom: 0.4rem; }
    .proj-desc  { font-size: 0.9rem; color: #CBD5E1; line-height: 1.7; }
    .tag        { display: inline-block; background: #1E293B; color: #A78BFA;
                  border-radius: 4px; padding: 2px 9px; font-size: 0.78rem; margin: 2px; }
    .impact     { background: #0F2A22; border-left: 3px solid #34D399;
                  border-radius: 0 8px 8px 0; padding: 8px 14px;
                  font-size: 0.88rem; color: #34D399; margin-top: 0.8rem; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Projects & Experience")
st.markdown("---")

# ── HERO PROJECT ─────────────────────────────────────────────────────
st.markdown("## ⭐ Featured Project — Gen AI Application")

st.markdown("""
<div class="proj-card-hero">
    <div class="proj-type">🔥 Internship Project — 2025–2026</div>
    <div class="proj-title">Public Transportation Delay Analysis </div>
    <div class="proj-desc">
        Built a full-stack <strong>Generative AI application</strong> integrating the
        <strong>Groq API (LLM inference)</strong> with a <strong>Streamlit</strong> front-end,
        developed entirely in <strong>VS Code</strong> with version control via <strong>GitHub</strong>.
        The application leverages large language models to solve a real business problem —
        enabling fast, AI-driven insights from structured data input.
        <br><br>
        <strong>What I did:</strong> Designed the LLM prompt architecture, built the Streamlit UI,
        managed API authentication, handled response parsing, and deployed the app with GitHub for
        version control and team collaboration.
    </div>
    <div class="impact">

- **Reduced delay diagnosis time by enabling real-time root cause analysis** — identified Rain and Thunderstorm weather as the top delay drivers (30.2 min avg) and Evening Rush as peak disruption period, giving transport operators actionable intelligence to prioritize fleet deployment.

- **Projected ₹1,099/month revenue uplift** through subscription gap analysis across Free, Basic, and Premium tiers, while achieving 89% on-time performance tracking across 20,000 trips and 20 Hyderabad routes.
    </div>
    <br>
    <span class="tag">Groq API</span>
    <span class="tag">Plotly</span>
    <span class="tag">Streamlit</span>
    <span class="tag">Python</span>
    <span class="tag">VS Code</span>
    <span class="tag">GitHub</span>
    <span class="tag">Gen AI</span>
    <span class="tag">Prompt Engineering</span>
</div>
""", unsafe_allow_html=True)

# ── INTERNSHIP 2 ──────────────────────────────────────────────────────
st.markdown("## 💼 Internship Experience")

st.markdown("""
<div class="proj-card">
    <div class="proj-type-blue">Data Science Intern - Feb,2026 -(present)</div>
    <div class="proj-title">Data Science Intern - SocialTeK AI & ML Business Solutions</div>
    <div class="proj-desc">
        Accomplished operational insight delivery for large-scale event management, measured by identifying actionable patterns across 20,000+ data points, by executing end-to-end Python pipelines covering data collection, cleaning, validation, and statistical analysis.
Generated structured service-level reports and Power BI visualizations adopted by operations teams to support safety planning, incident response, and contingency decision-making.
Maintained 100% data accuracy across all project deliverables and ensured on-time delivery of analytics outputs by implementing structured data validation workflows.
Collaborated cross-functionally with team members to align analytics outputs with operational requirements and organizational timelines.
    </div>
    <div class="impact">

- **Built and deployed a public transport delay analytics platform** as a Data Science Intern, applying Python, Pandas, and Plotly to analyze 20,000+ trip records across Hyderabad, uncovering key delay drivers — weather and peak-hour congestion — that improved on-time performance tracking to 89% across 20 routes.
    </div>
    <br>
    <span class="tag">Python</span>
    <span class="tag">PowerBi</span>
    <span class="tag">Excel</span>
     <span class="tag">Statistics</span>
    <span class="tag">Data Analytics</span>
    <span class="tag">Machine Learning</span>
    <span class="tag">Groq AI Integration</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="proj-card">
    <div class="proj-type-blue">Job Simulation — March 2026</div>
    <div class="proj-title">Data Analytics Job Simulation — Deloitte Australia (Forage)</div>
    <div class="proj-desc">
        Completed Deloitte's official data analytics & forensic technology job simulation.
        Built a <strong>Tableau dashboard</strong> to communicate key business findings to stakeholders.
        Used <strong>Excel</strong> to classify and segment data, and drew concrete business conclusions
        from forensic analysis — replicating real consulting analyst work.
    </div>
    <div class="impact">
    - Demonstrated consulting-grade analysis skills; produced a client-ready dashboard
        in the style of a Big 4 data analyst.
    </div>
    <br>
    <span class="tag">Tableau</span>
    <span class="tag">Excel</span>
    <span class="tag">Data Analytics</span>
    <span class="tag">Forensic Analysis</span>
    <span class="tag">Business Intelligence</span>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── ACADEMIC / PERSONAL PROJECTS ─────────────────────────────────────
st.markdown("## 🎓 Academic & Personal Projects")

placeholder_projects = [
    {
        "title": "📌 AI Based Resume Screening System ",
        "type": "MCA Final year Project — 2026",
        "desc": "Accomplished automated candidate-JD matching at scale, measured by sub-3-second real-time LLM inference, by engineering multi-step prompt pipelines using Claude Sonnet that extract match scores, missing keywords, and recruiter red flags.Designed end-to-end GenAI ownership — from system prompt architecture and context injection to Streamlit deployment — demonstrating full-stack Conversational AI development.",
        "tags": ["Python", "ML", "Gemini AI API", "Pandas", "Streamlit"]
    },
    {
        "title": "📌 Vegetable Detection Using OpenCV Python",
        "type": "Computer Vision Project",
        "desc": "Built a real-time vegetable detection system using OpenCV and Python, covering the full ML pipeline from data collection to model validation. Collected, cleaned, and preprocessed image datasets, then iteratively evaluated and improved detection model accuracy. Produced end-to-end technical documentation covering methodology, model performance metrics, and project findings.",
        "tags": ["Python", "OpenCV", "Haarcascade Trainer"],
    },
]

for proj in placeholder_projects:
    st.markdown(f"""
    <div class="proj-card" style="border: 1px dashed #334155;">
        <div class="proj-type-blue">{proj['type']}</div>
        <div class="proj-title" style="color:#F1F5F9;">{proj['title']}</div>
        <div class="proj-desc" style="color:#F1F5F9;">{proj['desc']}</div>
        <div>{''.join(f'<span class="tag" style="colour:#A78BFA">{t}</span>' for t in proj['tags'])}</div>
    """, unsafe_allow_html=True)
