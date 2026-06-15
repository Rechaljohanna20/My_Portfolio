import streamlit as st
import os

st.set_page_config(page_title="Resume | Rechal Johanna", page_icon="📄", layout="wide")

st.title("📄 Resume")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Rechal Johanna Ramakuri")
    st.markdown("**Data Analyst | MCA Student | AI Enthusiast**")
    st.markdown("📍 Hyderabad, Telangana &nbsp;|&nbsp; 📧 rechaljohanna@gmail.com &nbsp;|&nbsp; 📞 +91 88865 21738")
    st.markdown("---")

    st.markdown("#### 🎓 Education")
    st.markdown("""
    - **M.C.A** — SRM Institute of Science & Technology, Chennai *(2024 – 2026, GPA: 9.8(upto 3rd sem))*
    - **B.Sc Computer Science** — Sir C R Reddy College For Women, Eluru *(2021–2024, GPA: 8.0)*
    """)

    st.markdown("#### 💼 Experience")
    st.markdown("""
    - **Data Science Intern – SocialTek AI & ML Business Solutions** *(Feb 2026 - (present))*: Python, MS Excel, PowerBI, ML, Gen Ai
    - **Data Analytics Job Simulation – Deloitte Australia (Forage)** *(Mar 2026)*: Tableau dashboard, Excel analysis
    """)

    st.markdown("#### 🛠️ Skills")
    st.markdown("""
    Python · SQL · Power BI · MS Excel · Tableau · OpenCV · MySQL · M365 PowerApps ·
    Data Analysis · Database Management · OOP Concepts
    """)

    st.markdown("#### 🏅 Certifications")
    st.markdown("""
    - Data Analytics Job Simulation – Deloitte Australia (Forage), Mar 2026
    - SQL Certificate – Simplilearn
    """)

    st.markdown("#### 🏆 Achievements")
    st.markdown("""
    - 1st Place – Grand Talent Test, Sreedhar's Institute
    - Analyzed 500+ data records to identify patterns
    """)

with col2:
    st.markdown("### ⬇️ Download Resume")

    resume_path = "assets/Rechal_Johanna_Ramakuri_Resume.pdf"

    if os.path.exists(resume_path):
        with open(resume_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📥 Download PDF Resume",
            data=pdf_bytes,
            file_name="Rechal_Johanna_Ramakuri_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.info("📎 Place your resume PDF at:\n`assets/Rechal_Johanna_Ramakuri_Resume.pdf`\n\nThen this button will auto-enable.")

    st.markdown("---")
    st.markdown("### 📊 Profile Stats")
    st.metric("GPA", "9.8 / 10")
    st.metric("Internships", "2")
    st.metric("Certifications", "2+")
    st.metric("Records Analyzed", "500+")

st.markdown("---")
