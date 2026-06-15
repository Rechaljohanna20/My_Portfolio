import streamlit as st

st.set_page_config(page_title="Certificates | Rechal Johanna", page_icon="🏅", layout="wide")

st.markdown("""
<style>
    .cert-card {
        background: #0F172A; border: 1px solid #1E293B;
        border-radius: 12px; padding: 1.3rem 1.5rem; margin-bottom: 1rem;
    }
    .cert-card-highlight {
        background: linear-gradient(135deg,#1E1B4B,#0F2A22);
        border: 1.5px solid #A78BFA;
        border-radius: 12px; padding: 1.3rem 1.5rem; margin-bottom: 1rem;
    }
    .cert-badge   { display: inline-block; background: #064E3B; color: #34D399;
                    border-radius: 20px; padding: 2px 12px; font-size: 0.76rem;
                    font-weight: 700; margin-bottom: 0.6rem; }
    .cert-title   { font-size: 1.05rem; font-weight: 700; color: #F1F5F9; }
    .cert-issuer  { font-size: 0.9rem;  color: #A78BFA; margin: 0.2rem 0; }
    .cert-meta    { font-size: 0.82rem; color: #94A3B8; }
    .cert-desc    { font-size: 0.88rem; color: #CBD5E1; margin-top: 0.6rem; line-height:1.6; }
    .next-cert    { background: #1C1917; border: 1px dashed #92400E;
                    border-radius: 12px; padding: 1rem 1.4rem; margin-bottom: 0.8rem; }
</style>
""", unsafe_allow_html=True)

st.title("🏅 Certifications & Credentials")
st.markdown("---")

# ── Earned ────────────────────────────────────────────────────────────
st.markdown("## ✅ Earned Certifications")

st.markdown("""
<div class="cert-card-highlight">
    <div class="cert-badge">⭐ Job Simulation </div>
    <div class="cert-title">Data Analytics Job Simulation</div>
    <div class="cert-issuer">🏢 Deloitte Australia &nbsp;·&nbsp; via Forage</div>
    <div class="cert-meta">📅 March 2026 &nbsp;|&nbsp; 🛠 Tableau, Excel, Forensic Data Analysis</div>
    <div class="cert-desc">
        Completed Deloitte's official virtual analytics simulation. Built a Tableau dashboard for
        client reporting and used Excel for forensic data classification.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cert-card">
    <div class="cert-badge">Technical Certification</div>
    <div class="cert-title">SQL Certificate</div>
    <div class="cert-issuer">🏢 Simplilearn</div>
    <div class="cert-meta">📅 2025 &nbsp;|&nbsp; 🛠 SQL queries, joins, subqueries, MySQL</div>
    <div class="cert-desc">
        Industry-recognized SQL certification validating ability to write complex queries,
        design schemas, and manage relational databases.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cert-card">
    <div class="cert-badge">Technical Certification</div>
    <div class="cert-title">Data Science & AI Certificate</div>
    <div class="cert-issuer">🏢 SocialPrachar</div>
    <div class="cert-meta">📅 2026 &nbsp;|&nbsp; 🛠 SQL, Python, PowerBi, MS Excel, ML & AI</div>
    <div class="cert-desc">
        Able to write complex queries, Create Dashboards, manage relational databases and Developed a full-stack AI Integrated Public Transportation Delay Analytics Application using python and Streamlit.
    </div>
</div>
""", unsafe_allow_html=True)
