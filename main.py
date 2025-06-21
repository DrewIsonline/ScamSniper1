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
if "result" in st.session_state and st.session_state.result:
    ai_result_text = st.session_state.result.get("ai_result", "").lower()

    # Positive signal phrases – safe email indicators
    safe_indicators = [
        "does not appear to be a scam",
        "legitimate source",
        "this email is not a scam",
        "trusted company",
        "verified sender",
        "no signs of fraud",
        "no scam detected"
    ]

    # Scam signal phrases – red flag indicators
    scam_indicators = [
        "this is a scam",
        "scam detected",
        "this appears to be a scam",
        "this may be a phishing attempt",
        "fraudulent email",
        "request for personal information",
        "pressure tactic"
    ]

    # Default fallback
    display_text = st.session_state.result.get("ai_result", "")

    if any(phrase in ai_result_text for phrase in scam_indicators):
        st.error(f"⚠️ Scam Detected:\n\n{display_text}")
    elif any(phrase in ai_result_text for phrase in safe_indicators):
        st.success(f"✅ No scam detected.\n\n{display_text}")
    else:
        st.info(f"⚠️ Be cautious:\n\n{display_text}")


# Clear input
if st.button("🧹 Clear"):
    st.session_state.email_content = ""
    st.session_state.result = None

# Footer
st.markdown("---")
st.caption("Scam Sniper Agent v1 - From Drew Is: Tools to UpLevel the human experience.")
