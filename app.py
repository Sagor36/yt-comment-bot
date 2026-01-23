import streamlit as st
import google.generativeai as genai
import time

# এখানে আপনার আসল Gemini API Key বসান
API_KEY = "AIzaSyCFBexmiVj1MIs6wL1Yih4VtlF2YXcJ7vo"
genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন
def get_model():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        flash_models = [m for m in models if "flash" in m]
        return genai.GenerativeModel(flash_models[0] if flash_models else models[0])
    except:
        return genai.GenerativeModel('gemini-1.5-flash')

# Page Setup
st.set_page_config(page_title="SAGOR AI STUDIO", page_icon="🚀", layout="centered")

# Custom UI Design with High Contrast Colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Orbitron:wght@700&display=swap');
    
    body { background-color: #050a14; color: white; }
    .stApp { background-color: #050a14; }
    
    /* 1. Exclusive Header Border */
    .exclusive-header {
        border: 6px solid #FF0000;
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        background: rgba(255, 0, 0, 0.15);
        font-size: 35px;
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF;
        margin-bottom: 30px;
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.6);
        text-shadow: 2px 2px 5px #000;
    }

    /* 2. Large Input Label */
    .input-label {
        font-size: 28px;
        font-weight: bold;
        color: #00FFCC;
        margin-bottom: 15px;
        display: block;
        text-align: center;
        text-shadow: 0 0 10px #00FFCC;
    }

    /* 3. Action Button Customization */
    div.stButton > button {
        width: 100%;
        height: 80px;
        font-size: 26px !important;
        font-weight: 800;
        color: white;
        background: linear-gradient(90deg, #FF0000, #FF5F6D);
        border: 4px solid #FFFFFF;
        border-radius: 20px;
        text-transform: uppercase;
        box-shadow: 0 10px 20px rgba(255, 0, 0, 0.4);
    }

    /* 4. Result Card with Strong Border & Bold Text */
    .result-card {
        border: 5px solid #00FF00;
        padding: 30px;
        border-radius: 20px;
        background: #000000;
        margin-top: 35px;
        box-shadow: 0 0 35px rgba(0, 255, 0, 0.4);
        animation: slideIn 1s ease-out;
    }
    .result-content {
        font-size: 22px;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.5;
    }
    .result-content b { color: #00FFCC; font-size: 24px; }

    /* 5. Developed By Glow Animation */
    @keyframes glow-blue {
        0% { box-shadow: 0 0 15px #00D2FF; border-color: #00D2FF; }
        50% { box-shadow: 0 0 50px #00FFFF; border-color: #00FFFF; }
        100% { box-shadow: 0 0 15px #00D2FF; border-color: #00D2FF; }
    }
    .dev-section {
        border: 8px solid #00D2FF;
        padding: 25px;
        border-radius: 80px;
        text-align: center;
        margin-top: 60px;
        font-size: 45px;
        font-weight: 900;
        color: #FFFFFF;
        background: rgba(0, 210, 255, 0.2);
        animation: glow-blue 2s infinite ease-in-out;
        font-family: 'Orbitron', sans-serif;
    }

    /* 6. WhatsApp Button */
    .wa-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(90deg, #25D366, #075E54);
        color: white !important;
        padding: 22px;
        border-radius: 60px;
        text-decoration: none;
        font-size: 26px;
        font-weight: bold;
        margin-top: 40px;
        box-shadow: 0 10px 25px rgba(37, 211, 102, 0.5);
    }

    /* Loading Message Styling */
    .loading-text {
        font-size: 24px;
        color: #FFD700;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        text-shadow: 0 0 10px #FFD700;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.markdown('<div class="exclusive-header">🚀 SAGOR AI CONTENT STUDIO</div>', unsafe_allow_html=True)

# Input
st.markdown('<span class="input-label">Paste Video Transcript Below:</span>', unsafe_allow_html=True)
transcript = st.text_area("", height=250, placeholder="Paste here...", key="input_area")

# Generate Button
if st.button("🚀 GENERATE MESSAGE AND COMMENT"):
    if transcript:
        # Loading message as requested
        loading_placeholder = st.empty()
        loading_placeholder.markdown('<div class="loading-text">⏳ SAGOR WEB WORKING PLEASE WAIT FEW SEC...</div>', unsafe_allow_html=True)
        
        try:
            model = get_model()
            prompt = (
                "Transcript analysis request:\n"
                "1. Personal appreciation message (exactly 1.5 to 2 lines long).\n"
                "2. 5 short, creative YouTube comments in English.\n"
                f"Transcript: {transcript}"
            )
            response = model.generate_content(prompt)
            
            # Remove loading text and show result
            loading_placeholder.empty()
            
            st.markdown(f"""
            <div class="result-card">
                <div style="color: #00FF00; font-size: 28px; font-weight: bold; margin-bottom: 20px;">✅ SUCCESS! YOUR CONTENT:</div>
                <div class="result-content">
                    {response.text.replace('**', '<b>').replace('\n', '<br>')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            loading_placeholder.empty()
            st.error(f"Something went wrong! Error: {e}")
    else:
        st.warning("Please paste a transcript first!")

# Developer Info
st.markdown('<div class="dev-section">Developed By: SAGOR</div>', unsafe_allow_html=True)

# Contact Button
st.markdown('<a href="https://wa.link/kp3qzu" target="_blank" class="wa-btn">💬 CHAT ON WHATSAPP</a>', unsafe_allow_html=True)

# Large Footer Version
st.write("")
st.markdown('<div style="text-align:center; color:#555; font-size:22px; font-weight:bold; margin-top:50px;">PREMIUM V3.0 | 2026 ADVANCED EDITION</div>', unsafe_allow_html=True)
