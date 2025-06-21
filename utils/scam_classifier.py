from openai import OpenAI
import os
import streamlit as st

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY"))

def ai_check_email(email_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're a scam detection expert. Respond with an analysis of the email content and whether it's likely a scam."},
                {"role": "user", "content": f"Is this email a scam?\n\n{email_text}"}
            ]
        )

        answer = response.choices[0].message.content.strip()
        is_scam = any(word in answer.lower() for word in ["yes", "definitely", "likely", "scam"])

        return {
            "is_scam": is_scam,
            "ai_result": answer
        }

    except Exception as e:
        return {
            "is_scam": False,
            "ai_result": f"⚠️ Error during AI analysis: {str(e)}"
        }
