import streamlit as st

# Page configuration
st.set_page_config(page_title="Fresh Fruit Detector", layout="wide")

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# Title Section
st.markdown("<h1 class='title-text'>🍓 Fresh Fruit Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Detect the freshness of fruits instantly using AI 🍎</p>", unsafe_allow_html=True)

# --- Dashboard Layout using Streamlit Columns ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class='dashboard-card'>
        <div class='dashboard-icon'>🍎</div>
        <h3>Start Detection</h3>
        <p>Upload fruit images and detect freshness in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='dashboard-card'>
        <div class='dashboard-icon'>📊</div>
        <h3>View Results</h3>
        <p>Download predictions and confidence scores as CSV.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='dashboard-card'>
        <div class='dashboard-icon'>💡</div>
        <h3>About AI</h3>
        <p>Learn how the AI model classifies fruits as Fresh or Rotten.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    © 2025 Fresh Fruit Detector | Made with 🍓 by Team Innovators
</div>
""", unsafe_allow_html=True)
