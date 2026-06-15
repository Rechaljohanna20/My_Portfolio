import streamlit as st

st.set_page_config(page_title="About | Rechal Johanna", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>
    .edu-card {
        background: #1A1A2E;
        border-left: 4px solid #7F77DD;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .edu-title { font-size: 1.1rem; font-weight: 700; color: #FFFFFF; }
    .edu-inst  { font-size: 0.95rem; color: #7F77DD; }
    .edu-meta  { font-size: 0.85rem; color: #9FA6B2; margin-top: 0.3rem; }
    .highlight { color: #5DCAA5; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

st.title("👩‍💻 About Me")
st.markdown("---")

# --- Personal Summary ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("### Summary")
    st.write("""
    I'm **Rechal Johanna Ramakuri**, a detail-oriented Computer Science graduate currently pursuing
    my **MCA at SRM Institute of Science & Technology, Chennai** with a GPA of 9.8.

    I have hands-on experience in Data Collection, Interpretation, and Analytical Problem Solving
    through academic projects and internships — including a real-world internship using **OpenCV + Python**
    and a **Deloitte Data Analytics Job Simulation** on Forage.

    I thrive in both team and independent settings and am passionate about using data and AI
    to solve real business problems.
    """)

with col2:
    st.markdown("### Quick Info")
    st.markdown("📍 **Location:** Hyderabad, Telangana")
    st.markdown("📧 **Email:** rechaljohanna@gmail.com")
    st.markdown("📞 **Phone:** +91 88865 21738")
    st.markdown("🌐 **LinkedIn:** [rechaljohannaramakuri](https://www.linkedin.com/in/rechaljohannaramakuri/)")
    st.markdown("🗣️ **Languages:** English, Telugu")
    st.markdown("🎨 **Interests:** Drawing, Cooking, Making Crafts")

st.markdown("---")

# --- Education ---
st.markdown("### 🎓 Education")

st.markdown("""
<div class="edu-card">
    <div class="edu-title">Master of Computer Application (M.C.A)</div>
    <div class="edu-inst">SRM Institute of Science & Technology, Chennai</div>
    <div class="edu-meta">
        📅 2024 – Pursuing &nbsp;|&nbsp; 🌐 Virtual Mode &nbsp;|&nbsp;
        <span class="highlight">GPA: 9.8 / 10 (Up to 3rd Sem)</span>
    </div>
    <div class="edu-meta" style="margin-top:0.6rem;">
        Relevant coursework: Database Management, Data Analytics, Machine Learning,
        Research Methodology, OOP with Python, Cloud Computing
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
    </div>
    <div class="edu-meta" style="margin-top:0.6rem;">
        Relevant coursework: Data Structures, Algorithms, Database Systems, Statistics,
        Operating Systems, Computer Networks
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Awards ---
st.markdown("### 🏆 Awards & Achievements")
col1, col2 = st.columns(2)
with col1:
    st.success("🥇 **1st Place** – Grand Talent Test, Sreedhar's Institute")
    st.info("📊 Analyzed **500+ data records** to identify patterns and business insights")
with col2:
    st.success("🎓 **9.8 GPA** – Top performer in MCA program at SRM")
    st.info("🔬 Completed **Deloitte Australia** Data Analytics Job Simulation (Forage)")

st.markdown("---")

# --- Add Your Own Details ---
st.markdown("### ✏️ Want to add more?")
st.markdown("Add your academic projects, thesis title, seminars attended, or extra activities below:")

with st.expander("➕ Add Academic Project / Activity"):
    proj_title = st.text_input("Title")
    proj_desc  = st.text_area("Description")
    proj_year  = st.text_input("Year")
    if st.button("Save (customize in code)"):
        st.success(f"Add this to the code: Title='{proj_title}', Year='{proj_year}'")
