import streamlit as st

st.set_page_config(
    page_title="Rechal Johanna | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #7F77DD, #5DCAA5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #9FA6B2;
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        background-color: #1A1A2E;
        color: #7F77DD;
        border: 1px solid #7F77DD;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.85rem;
        margin: 4px;
    }
    .section-divider {
        border-top: 1px solid #2D2D44;
        margin: 2rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #1A1A2E;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("## Rechal Johanna")
    st.markdown("📍 Hyderabad, Telangana")
    st.markdown("📧 rechaljohanna@gmail.com")
    st.markdown("📞 +91 88865 21738")
    st.markdown("---")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/rechaljohannaramakuri/)")
    st.markdown("---")
    st.caption("Built with Streamlit 🚀")

# --- Hero Section ---
st.markdown('<p class="main-header">Rechal Johanna Ramakuri</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Analyst | AI Enthusiast | MCA @ SRM Institute</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("GPA", "9.8 / 10", "MCA – SRM")
with col2:
    st.metric("Experience", "2", "Internships")
with col3:
    st.metric("Certifications", "2+", "Industry certs")
with col4:
    st.metric("Records Analyzed", "500+", "Data points")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --- Quick Summary ---
st.markdown("### 👋 About Me")
st.info("""
Detail-oriented Computer Science graduate with strong skills in **Data Analysis, SQL, Python, Power BI** and AI/ML.
Hands-on experience in Data Collection, Interpretation, and Analytical Problem Solving through academic projects and internships.
Ready to leverage academic knowledge to contribute to impactful projects in a tech-driven organization.
""")

# --- Quick Skill Tags ---
st.markdown("### 🛠️ Core Skills")
skills = ["Python", "SQL", "Power BI", "MS Excel", "OpenCV", "Tableau",
          "Data Analysis", "Jupyter Notebook", "MySQL", "M365 PowerApps"]
cols = st.columns(5)
for i, skill in enumerate(skills):
    with cols[i % 5]:
        st.markdown(f'<span class="badge">{skill}</span>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("#### 👈 Use the sidebar to explore my Projects, Skills, Certificates and more!")
