import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন
def get_model():
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    return genai.GenerativeModel(models[0])

# Page Setup
st.set_page_config(page_title="YT AI Studio", page_icon="🚀", layout="centered")

# Custom Premium CSS
st.markdown("""
    <style>
    body { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; }
    
    /* exclusive Title Border */
    .exclusive-header {
        border: 4px double #FF4B4B;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        background: rgba(255, 75, 75, 0.1);
        font-size: 32px;
        font-weight: bold;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.4);
    }

    /* Action Box */
    .action-box {
        border: 2px solid #ffffff33;
        padding: 20px;
        border-radius: 15px;
        background: #161b22;
        margin-top: 20px;
    }

    /* Developed By Border */
    .dev-section {
        border: 5px solid #1E90FF;
        padding: 20px;
        border-radius: 50px;
        text-align: center;
        margin-top: 50px;
        font-size: 35px;
        font-family: 'Arial Black', sans-serif;
        color: #1E90FF;
        background: rgba(30, 144, 255, 0.05);
        box-shadow: 0 0 15px rgba(30, 144, 255, 0.5);
    }

    /* WhatsApp Button */
    .wa-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(90deg, #25D366, #128C7E);
        color: white !important;
        padding: 15px;
        border-radius: 30px;
        text-decoration: none;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        transition: 0.3s;
    }
    .wa-btn:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(37, 211, 102, 0.4); }
    
    /* Success Message Box */
    .output-card {
        background: #21262d;
        border-left: 5px solid #25D366;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Exclusive Title
st.markdown('<div class="exclusive-header">🎥 YOUTUBE MESSAGE & COMMENT AI</div>', unsafe_allow_html=True)

# Input
transcript = st.text_area("Paste Video Transcript Below:", height=200, placeholder="Enter transcript here...")

# 2. Generate Button Area
st.markdown('<div class="action-box">', unsafe_allow_html=True)
if st.button("✨ GENERATE MESSAGE AND COMMENT"):
    if transcript:
        with st.spinner('🤖 AI Thinking...'):
            try:
                model = get_model()
                # Message 1.5/2 lines instruction
                prompt = (
                    "Based on this YouTube transcript, generate:\n"
                    "1. APPRECIATION MESSAGE: A warm personal message exactly 1.5 to 2 lines long thanking the creator.\n"
                    "2. 5 COMMENTS: Polite English comments for the video.\n"
                    f"Transcript: {transcript}"
                )
                response = model.generate_content(prompt)
                
                st.markdown('<div class="output-card">', unsafe_allow_html=True)
                st.subheader("✅ Your Content Ready:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {e}. Please check your API Key.")
    else:
        st.warning("Please paste a transcript first!")
st.markdown('</div>', unsafe_allow_html=True)

# 3. Developer Info with Large Border
st.markdown('<div class="dev-section">Developed By: SAGOR</div>', unsafe_allow_html=True)

# WhatsApp Button
st.markdown('<a href="https://wa.link/kp3qzu" target="_blank" class="wa-btn">💬 Contact Me on WhatsApp</a>', unsafe_allow_html=True)

st.write("")
st.caption("Premium Edition | v2.0 | Advanced Content Generator")
