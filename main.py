import streamlit as st
from utils.scam_classifier import ai_check_email
from PIL import Image
import os

# Initialize session state
if "email_content" not in st.session_state:
    st.session_state.email_content = ""

if "result" not in st.session_state:
    st.session_state.result = None

# Page configuration
st.set_page_config(page_title="Scam Sniper Agent", layout="centered")

# Load and display logo
logo_path = os.path.join("assets", "drewis_logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=100)

# Title
st.title("Scam Sniper Agent v1")

# Manual input
st.markdown("### 📧 Paste Email Manually")
email_content = st.text_area("Paste suspicious email text here:", value=st.session_state.email_content, height=200)

# Scan action
if st.button("🔍 Scan for Scams"):
    if not email_content.strip():
        st.warning("Please paste some email content first.")
    else:
        result = ai_check_email(email_content)
        st.session_state.email_content = email_content
        st.session_state.result = result

# Display result
if st.session_state.result:
    if st.session_state.result.get("is_scam"):
        st.error(f"⚠️ Scam Detected:\n\n{st.session_state.result.get('ai_result', '')}")
    else:
        st.success(f"✅ No scam detected.\n\n{st.session_state.result.get('ai_result', '')}")

# Clear input
if st.button("🧹 Clear"):
    st.session_state.email_content = ""
    st.session_state.result = None

# Footer
st.markdown("---")
st.caption("Scam Sniper Agent v1 - From Drew Is: Tools to UpLevel the human experience.")
