import streamlit as st

st.set_page_config(page_title="Contact | Rechal Johanna", page_icon="📬", layout="wide")

st.title("📬 Contact Me")
st.markdown("---")
st.markdown("#### I'm actively looking for Data Analyst opportunities. Let's connect!")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📋 Contact Details")
    st.markdown("""
    | | |
    |---|---|
    | 📧 **Email** | rechaljohanna@gmail.com |
    | 📞 **Phone** | +91 88865 21738 |
    | 📍 **Location** | Hyderabad, Telangana – 500072 |
    | 💼 **LinkedIn** | [rechaljohannaramakuri](https://www.linkedin.com/in/rechaljohannaramakuri/) |
    | 🐙 **GitHub** | Add your GitHub link here |
    """)

    st.markdown("---")
    st.markdown("### 🌐 Connect on Social")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rechaljohannaramakuri/)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com)")
    st.markdown("[![Email](https://img.shields.io/badge/Email-Send%20Mail-D14836?style=for-the-badge&logo=gmail)](mailto:rechaljohanna@gmail.com)")

with col2:
    st.markdown("### ✉️ Send Me a Message")
    st.caption("Fill this form to reach out directly (customize with EmailJS or Formspree for live emails).")

    name    = st.text_input("Your Name")
    email   = st.text_input("Your Email")
    subject = st.selectbox("Subject", [
        "Job Opportunity",
        "Internship Offer",
        "Collaboration / Project",
        "Feedback on Portfolio",
        "Other"
    ])
    message = st.text_area("Message", height=150)

    if st.button("Send Message 📨"):
        if name and email and message:
            st.success(f"Thanks {name}! Your message has been noted. I'll reply to {email} soon.")
            st.balloons()
        else:
            st.warning("Please fill in all fields before sending.")

st.markdown("---")
st.markdown("### 📅 Availability")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.success("✅ Open to full-time roles")
with col_b:
    st.success("✅ Open to internships")
with col_c:
    st.info("🕐 Response time: within 24 hrs")
