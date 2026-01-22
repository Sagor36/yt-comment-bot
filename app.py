import streamlit as st
import google.generativeai as genai

# Ekhane apnar Gemini API Key-ti boshan
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

def get_working_model():
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if 'models/gemini-1.5-flash' in available_models:
        return genai.GenerativeModel('gemini-1.5-flash')
    return genai.GenerativeModel('gemini-pro')

# Page Layout
st.set_page_config(page_title="YT Feedback Tool", page_icon="🎥", layout="centered")

# Custom CSS for Exclusive Design
st.markdown("""
    <style>
    .main-title {
        border: 4px solid #FF0000;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background-color: #f9f9f9;
        color: #FF0000;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(255, 0, 0, 0.2);
    }
    .dev-border {
        border: 3px dashed #1E90FF;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        font-size: 24px;
        font-weight: bold;
        color: #1E90FF;
        background-color: #f0f8ff;
    }
    .whatsapp-btn {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #25D366;
        color: white !important;
        padding: 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }
    .generate-box {
        border: 2px solid #333;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Header (Exclusive Border Title)
st.markdown('<div class="main-title">🎥 YOUTUBE APPRECIATION & COMMENT GENERATOR</div>', unsafe_allow_html=True)
st.write("") 

# Transcript Input
transcript = st.text_area("Video Transcript Ekhane Paste Korun:", height=200)

# 2. Action Button with Border Design
st.markdown('<div class="generate-box">', unsafe_allow_html=True)
if st.button("🚀 GENERATE MESSAGE AND COMMENT"):
    if transcript:
        with st.status("AI Analyzing...", expanded=False):
            try:
                model = get_working_model()
                # Message length 1.5/2 line-er instruction deya hoyeche
                prompt = (
                    "Based on the transcript, generate:\n"
                    "1. A PERSONAL MESSAGE: Max 2 short sentences (1.5 to 2 lines). Make it extremely appreciative.\n"
                    "2. 5 SHORT COMMENTS: Engaging and polite English comments.\n"
                    f"Transcript: {transcript}"
                )
                response = model.generate_content(prompt)
                st.success("Results Ready!")
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste a transcript first!")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Developer Info with Big Border & WhatsApp Button
st.markdown('<div class="dev-border">Developed By: SAGOR</div>', unsafe_allow_html=True)
st.markdown('<a href="https://wa.link/kp3qzu" target="_blank" class="whatsapp-btn">💬 Contact Me on WhatsApp</a>', unsafe_allow_html=True)

st.write("")
st.caption("Powered by SAGOR DEVOLOPER | Fast & Exclusive Edition")
