import streamlit as st
import requests

st.set_page_config(page_title="Contact | Rechal Johanna Ramakuri", page_icon="📬", layout="wide")
FORMSPREE_URL = "https://formspree.io/f/xlgkzoya"
st.title("📬 Contact Me")
st.markdown("#### Actively seeking Data Scientist / ML Engineer roles — available immediately.")
st.markdown("---")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("### 📋 Reach Me At")
    st.markdown("""
    | | |
    |---|---|
    | 📧 **Email** | rechaljohanna@gmail.com |
    | 📞 **Phone** | +91 88865 21738 |
    | 📍 **Location** | Hyderabad, Telangana – 500082 |
    | 💼 **LinkedIn** | [rechaljohannaramakuri](https://www.linkedin.com/in/rechaljohannaramakuri/) |
    | 🐙 **GitHub** | [Rechaljohanna20](https://github.com/Rechaljohanna20) |
    """)
    st.markdown("---")
    st.markdown("### 🌐 Socials")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rechaljohannaramakuri/)")
    st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rechaljohanna@gmail.com)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)](https://github.com/Rechaljohanna20)")

    st.markdown("---")
    st.markdown("### 📅 Availability")
    st.success("✅ Available for full-time roles")
    st.success("✅ Open to hybrid / remote positions")
    st.info("⚡ Response time: within 24 hours")

with col2:
    st.markdown("### ✉️ Send a Message")
    st.caption("This form sends directly to my Gmail inbox.")
    name    = st.text_input("Your Name")
    email   = st.text_input("Your Email")
    company = st.text_input("Company / Organization (optional)")
    subject = st.selectbox("Regarding", [
        "Job Opportunity — Data Scientist",
        "Job Opportunity — AI/ML Engineer",
        "Job Opportunity — Data Analyst",
        "Internship Offer",
        "Collaboration / Project",
        "Feedback on Portfolio",
        "Other"
    ])
    message = st.text_area("Message", height=140)

    if st.button("Send Message 📨", use_container_width=True):
        # Validation
        if not name.strip():
            st.warning("⚠️ Please enter your name.")
        elif not email.strip() or "@" not in email:
            st.warning("⚠️ Please enter a valid email address.")
        elif subject == "-- Select a subject --":
            st.warning("⚠️ Please select a subject.")
        elif not message.strip() or len(message.strip()) == 0:
            st.warning("⚠️ Please write a message (at least 20 characters).")
        else:
            with st.spinner("Sending your message..."):
                try:
                    response = requests.post(
                        FORMSPREE_URL,
                        data={
                            "name":    name.strip(),
                            "email":   email.strip(),
                            "company": company.strip(),
                            "subject": subject,
                            "message": message.strip()
                        },
                        headers={"Accept": "application/json"},
                        timeout=10
                    )
                    if response.status_code == 200:
                        st.balloons()
                        st.markdown("""
                        <div class="success-box">
                            ✅ <strong>Message sent successfully!</strong><br>
                            Thanks for reaching out. I'll reply to your email within 24 hours.
                        </div>
                        """, unsafe_allow_html=True)

                    elif response.status_code == 422:
                        st.error("❌ Invalid email address. Please check and try again.")

                    else:
                        st.error(
                            f"❌ Something went wrong (status {response.status_code}). "
                            "Please email me directly at rechaljohanna@gmail.com"
                        )
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please try again or email me directly.")
                except requests.exceptions.ConnectionError:
                    st.error("🌐 No internet connection. Please check your network.")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {str(e)}")
