import streamlit as st

st.set_page_config(page_title="Skills | Rechal Johanna", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
    .skill-category { font-size: 1.05rem; font-weight: 700; color: #7F77DD; margin: 1.2rem 0 0.5rem; }
    .tool-badge {
        display: inline-block; background: #1A1A2E; color: #5DCAA5;
        border: 1px solid #5DCAA5; border-radius: 20px;
        padding: 5px 14px; font-size: 0.85rem; margin: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛠️ Skills & Tools")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Programming & Query Languages")

    st.markdown('<div class="skill-category">Python</div>', unsafe_allow_html=True)
    st.progress(80)
    st.caption("Pandas, NumPy, OpenCV, Jupyter Notebook")

    st.markdown('<div class="skill-category">SQL / MySQL</div>', unsafe_allow_html=True)
    st.progress(85)
    st.caption("Queries, joins, subqueries, MySQL Workbench")

    st.markdown('<div class="skill-category">MS Excel</div>', unsafe_allow_html=True)
    st.progress(85)
    st.caption("Pivot tables, VLOOKUP, data classification, charts")

    st.markdown('<div class="skill-category">M365 — PowerApps</div>', unsafe_allow_html=True)
    st.progress(65)
    st.caption("App building, automation with Microsoft Power Platform")

with col2:
    st.markdown("### Analytics & Visualization")

    st.markdown('<div class="skill-category">Power BI</div>', unsafe_allow_html=True)
    st.progress(75)
    st.caption("Dashboards, DAX basics, data modeling")

    st.markdown('<div class="skill-category">Tableau</div>', unsafe_allow_html=True)
    st.progress(70)
    st.caption("Interactive dashboards (Deloitte simulation)")

    st.markdown('<div class="skill-category">Data Analysis & Interpretation</div>', unsafe_allow_html=True)
    st.progress(85)
    st.caption("Pattern recognition, 500+ records analyzed")

    st.markdown('<div class="skill-category">Google Sheets</div>', unsafe_allow_html=True)
    st.progress(80)
    st.caption("Formulas, collaboration, data tracking")

st.markdown("---")

# --- Conceptual Skills ---
st.markdown("### 📚 Core Concepts")
concepts = [
    "Database Management", "Data Collection & Validation",
    "Research & Information Synthesis", "OOP Concepts",
    "Analytical Problem Solving", "Model Accuracy Evaluation",
    "Image Dataset Processing", "Business Intelligence",
    "Forensic Data Analysis", "Technical Documentation"
]
cols = st.columns(5)
for i, c in enumerate(concepts):
    with cols[i % 5]:
        st.markdown(f'<span class="tool-badge">{c}</span>', unsafe_allow_html=True)

st.markdown("---")

# --- Tools Ecosystem ---
st.markdown("### 🧰 Tools Ecosystem")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("**Development**")
    st.markdown("- Jupyter Notebook\n- VS Code\n- MySQL Workbench")
with c2:
    st.markdown("**Data & Analytics**")
    st.markdown("- Power BI\n- Tableau\n- MS Excel\n- Google Sheets")
with c3:
    st.markdown("**AI / CV**")
    st.markdown("- OpenCV\n- Python ML libs\n- NumPy / Pandas")
with c4:
    st.markdown("**Productivity**")
    st.markdown("- M365 PowerApps\n- GitHub\n- Google Workspace")

st.markdown("---")
st.info("💡 **Currently learning:** Advanced ML with Scikit-learn, Gen AI with LangChain, and Streamlit app development!")
