import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Rechal Johanna | Data Scientist",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Safe photo loader ─────────────────────────────────────────────────
def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

photo_b64 = img_to_base64("assets/profile.png")

# ── Build photo HTML safely ───────────────────────────────────────────
if photo_b64:
    hero_photo_html = (
        '<div class="photo-ring">'
        '<img src="data:image/png;base64,' + photo_b64 + '" alt="Rechal Johanna Ramakuri">'
        '</div>'
    )
    sidebar_photo_html = (
        '<img src="data:image/png;base64,' + photo_b64 + '" '
        'style="width:100%;height:100%;border-radius:50%;'
        'object-fit:cover;object-position:top;border:2px solid #0A0A18;">'
    )
else:
    hero_photo_html = '<div class="photo-ring-placeholder">👩‍💻</div>'
    sidebar_photo_html = '<div style="font-size:2.5rem;line-height:76px;">👩‍💻</div>'

# ── CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D0D1A 0%, #12122A 100%);
    border-right: 1px solid #1E1E3F;
}

.hero-wrapper {
    display: flex; align-items: center;
    gap: 48px; padding: 2.5rem 0 2rem;
}
.photo-ring {
    flex-shrink: 0; width: 220px; height: 220px; border-radius: 50%;
    background: linear-gradient(135deg, #7C3AED, #10B981, #3B82F6);
    padding: 4px;
    box-shadow: 0 0 40px rgba(124,58,237,0.4), 0 0 80px rgba(16,185,129,0.15);
}
.photo-ring img {
    width: 100%; height: 100%; border-radius: 50%;
    object-fit: cover; object-position: top;
    border: 3px solid #0A0A18;
}
.photo-ring-placeholder {
    flex-shrink: 0; width: 220px; height: 220px; border-radius: 50%;
    background: linear-gradient(135deg,#4C1D95,#065F46);
    display: flex; align-items: center; justify-content: center;
    font-size: 5rem;
    box-shadow: 0 0 40px rgba(124,58,237,0.4);
}
.hero-text { flex: 1; }
.hero-greeting {
    font-size: 0.95rem; font-weight: 600; letter-spacing: 0.12em;
    color: #10B981; text-transform: uppercase; margin-bottom: 6px;
}
.hero-name {
    font-size: 2.9rem; font-weight: 900; line-height: 1.1;
    background: linear-gradient(135deg, #A78BFA 0%, #34D399 50%, #60A5FA 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
}
.hero-role { font-size: 1.1rem; color: #94A3B8; font-weight: 500; margin-bottom: 14px; }
.hero-bubble {
    background: linear-gradient(135deg, rgba(30,27,75,0.9), rgba(6,78,59,0.6));
    border: 1px solid rgba(167,139,250,0.3);
    border-radius: 16px 16px 16px 4px;
    padding: 1rem 1.3rem;
    font-size: 0.95rem; color: #CBD5E1; line-height: 1.75;
    max-width: 580px; position: relative; margin-bottom: 18px;
}
.hero-bubble .green { color: #34D399; font-weight: 600; }
.stat-row { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 18px; }
.stat-pill {
    background: rgba(15,23,42,0.9); border: 1px solid #1E293B;
    border-radius: 40px; padding: 6px 16px;
    font-size: 0.82rem; color: #94A3B8;
    display: inline-flex; align-items: center; gap: 6px;
}
.stat-pill .val { font-weight: 700; color: #A78BFA; font-size: 0.95rem; }
.section-divider { border-top: 1px solid #1E293B; margin: 1.6rem 0; }
.avail-banner {
    background: linear-gradient(135deg, #064E3B 0%, #0F172A 100%);
    border: 1px solid #34D399; border-radius: 10px;
    padding: 10px 18px; font-size: 0.88rem; color: #34D399;
    margin-bottom: 1rem;
}
.badge-purple {
    display: inline-block; background: #1E1B4B; color: #A78BFA;
    border: 1px solid #3730A3; border-radius: 20px;
    padding: 4px 13px; font-size: 0.82rem; margin: 3px;
}
.badge-green {
    display: inline-block; background: #064E3B; color: #34D399;
    border: 1px solid #065F46; border-radius: 20px;
    padding: 4px 13px; font-size: 0.82rem; margin: 3px;
}
.badge-blue {
    display: inline-block; background: #1E3A5F; color: #60A5FA;
    border: 1px solid #1D4ED8; border-radius: 20px;
    padding: 4px 13px; font-size: 0.82rem; margin: 3px;
}

/* ── Navigation Buttons ── */
div.stButton > button {
    width: 100%;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 0.92rem;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: transform 0.15s, opacity 0.15s;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    opacity: 0.9;
}
div[data-testid="column"]:nth-child(1) div.stButton > button {
    background: linear-gradient(135deg, #7C3AED, #5B21B6);
    color: white;
}
div[data-testid="column"]:nth-child(2) div.stButton > button {
    background: transparent;
    color: #34D399;
    border: 1.5px solid #34D399 !important;
}
div[data-testid="column"]:nth-child(3) div.stButton > button {
    background: transparent;
    color: #60A5FA;
    border: 1.5px solid #3B82F6 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────
with st.sidebar:
    sidebar_html = (
        '<div style="text-align:center;padding:1rem 0 0.5rem;">'
        '<div style="width:80px;height:80px;border-radius:50%;'
        'background:linear-gradient(135deg,#7C3AED,#10B981);'
        'padding:2px;margin:0 auto 10px;overflow:hidden;">'
        + sidebar_photo_html +
        '</div>'
        '<div style="font-weight:700;font-size:1rem;color:#E2E8F0;">Rechal Johanna</div>'
        '<div style="font-size:0.78rem;color:#94A3B8;margin-top:2px;">Data Scientist · MCA 2026</div>'
        '</div>'
    )
    st.markdown(sidebar_html, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("📍 Hyderabad, Telangana")
    st.markdown("📧 rechaljohanna@gmail.com")
    st.markdown("📞 +91 88865 21738")
    st.markdown("---")
    st.markdown("**🔗 Connect:**")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/rechaljohannaramakuri/)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white&style=flat)](https://github.com)")
    st.markdown("---")
    st.markdown("**🟢 Open to:**")
    st.markdown("• Full-time Data Scientist roles")
    st.markdown("• ML / AI Engineer positions")
    st.markdown("• Remote & Hybrid opportunities")
    st.markdown("---")

# ── Hero ──────────────────────────────────────────────────────────────
hero_html = (
    '<div class="hero-wrapper">'
    + hero_photo_html +
    '<div class="hero-text">'
    '<div class="hero-greeting">👋 Hello, I\'m</div>'
    '<div class="hero-name">Rechal Johanna Ramakuri</div>'
    '<div class="hero-role">Data Analyst &nbsp;·&nbsp; Data Scientist &nbsp;·&nbsp; MCA Graduate 2026</div>'
    '<div class="hero-bubble">'
    'I\'m a <strong>2026 MCA graduate</strong> from SRM Institute (GPA <strong>9.8/10</strong>) '
    'with a passion for turning raw data into real decisions. I build '
    '<span class="green">Generative AI applications</span> using Groq API, Streamlit &amp; Python, '
    'and have real analytics exposure through a '
    '<strong>Deloitte Australia Data Analytics Simulation</strong>. '
    'I\'m ready to bring my <strong>ML + Gen AI + BI skills</strong> to a high-impact '
    'Data Scientist role. Let\'s build something great together! 🚀'
    '</div>'
    '<div class="stat-row">'
    '<div class="stat-pill">🎓 GPA <span class="val">9.8</span></div>'
    '<div class="stat-pill">💼 Internships <span class="val">2+</span></div>'
    '<div class="stat-pill">📊 Records <span class="val">500+</span></div>'
    '<div class="stat-pill">🤖 AI Tools <span class="val">5+</span></div>'
    '<div class="stat-pill">📅 Batch <span class="val">2026</span></div>'
    '</div>'
    '</div>'   
    '</div>'
)
st.markdown(hero_html, unsafe_allow_html=True)

# ── CTA Buttons (st.switch_page for real navigation) ─────────────────
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📄 Download Resume", use_container_width=True):
        st.switch_page("pages/6_resume.py")
with col2:
    if st.button("🚀 View Projects", use_container_width=True):
        st.switch_page("pages/2_projects.py")
with col3:
    if st.button("📬 Hire Me", use_container_width=True):
        st.switch_page("pages/5_contact.py")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Available Banner ──────────────────────────────────────────────────
st.markdown(
    '<div class="avail-banner">'
    '🟢 &nbsp;<strong>Currently available</strong> for full-time Data Scientist / ML Engineer roles'
    '&nbsp;·&nbsp; Hyderabad / Remote / Hybrid &nbsp;·&nbsp; Immediate joiner'
    '</div>',
    unsafe_allow_html=True
)

# ── Why Hire Me ───────────────────────────────────────────────────────
st.markdown("### 🎯 Why Hire Me?")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("**🧠 Gen AI Builder**\n\nBuilt real Gen AI apps with Groq API + Streamlit + Python. Most 2026 freshers can't say that.")
with c2:
    st.info("**📊 Analytics + ML Foundation**\n\nSQL, Pandas, Scikit-learn, Power BI, Tableau — full data pipeline from raw data to business insight.")
with c3:
    st.info("**🏢 Industry Exposure**\n\nDeloitte Australia simulation + computer vision internship = real-world problem solving, not just coursework.")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Tech Stack ────────────────────────────────────────────────────────
st.markdown("### 🔧 Tech Stack")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Data & ML**")
    st.markdown(
        '<span class="badge-purple">Python</span>'
        '<span class="badge-purple">SQL</span>'
        '<span class="badge-purple">Pandas</span>'
        '<span class="badge-purple">Scikit-learn</span>'
        '<span class="badge-purple">OpenCV</span>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown("**Gen AI & Apps**")
    st.markdown(
        '<span class="badge-green">Groq API</span>'
        '<span class="badge-green">LLMs</span>'
        '<span class="badge-green">Streamlit</span>'
        '<span class="badge-green">Prompt Engineering</span>'
        '<span class="badge-green">GitHub</span>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown("**Visualization**")
    st.markdown(
        '<span class="badge-blue">Power BI</span>'
        '<span class="badge-blue">Tableau</span>'
        '<span class="badge-blue">Matplotlib</span>'
        '<span class="badge-blue">MS Excel</span>'
        '<span class="badge-blue">Seaborn</span>',
        unsafe_allow_html=True
    )

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("#### 👈 Explore the sidebar — Projects, Skills, Certificates, Resume & Contact")
