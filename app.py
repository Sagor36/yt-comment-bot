import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"
genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন
def get_model():
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # gemini-1.5-flash থাকলে সেটা আগে নিবে
    flash_models = [m for m in models if "flash" in m]
    return genai.GenerativeModel(flash_models[0] if flash_models else models[0])

# Page Setup
st.set_page_config(page_title="YT AI Studio", page_icon="🚀", layout="centered")

# Custom UI Design with Animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
    
    body { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; }
    
    /* exclusive Title Border */
    .exclusive-header {
        border: 4px solid #FF4B4B;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        background: rgba(255, 75, 75, 0.1);
        font-size: 30px;
        font-weight: bold;
        color: #FF4B4B;
        margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(255, 75, 75, 0.5);
    }

    /* Input Label Styling */
    .input-label {
        font-size: 24px;
        font-weight: bold;
        color: #00D2FF;
        margin-bottom: 10px;
        display: block;
    }

    /* Action Box Button Animation */
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        font-weight: bold;
        color: white;
        background: linear-gradient(90deg, #FF4B4B, #FF8008);
        border: 2px solid white;
        border-radius: 15px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.7);
    }

    /* Developed By Animated Section */
    @keyframes glow {
        0% { box-shadow: 0 0 5px #1E90FF; border-color: #1E90FF; }
        50% { box-shadow: 0 0 30px #00D2FF; border-color: #00D2FF; }
        100% { box-shadow: 0 0 5px #1E90FF; border-color: #1E90FF; }
    }
    .dev-section {
        border: 6px solid #1E90FF;
        padding: 20px;
        border-radius: 60px;
        text-align: center;
        margin-top: 40px;
        font-size: 38px;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
        background: rgba(30, 144, 255, 0.15);
        animation: glow 2s infinite ease-in-out;
    }

    /* WhatsApp Button */
    .wa-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: #25D366;
        color: white !important;
        padding: 15px;
        border-radius: 40px;
        text-decoration: none;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
    }

    /* Footer Text */
    .footer-text {
        font-size: 18px;
        color: #888;
        text-align: center;
        margin-top: 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Title
st.markdown('<div class="exclusive-header">🎥 YOUTUBE MESSAGE & COMMENT AI</div>', unsafe_allow_html=True)

# 2. Input Label and Area
st.markdown('<span class="input-label">Paste Video Transcript Below:</span>', unsafe_allow_html=True)
transcript = st.text_area("", height=200, placeholder="এখানে ট্রান্সক্রিপ্ট পেস্ট করুন...", key="input")

# 3. Generate Message And Comment Button
if st.button("🚀 GENERATE MESSAGE AND COMMENT"):
    if transcript:
        with st.spinner('🤖 AI Analysis Korche...'):
            try:
                model = get_model()
                # 1.5/2 lines appreciation instruction
                prompt = (
                    "Using the following transcript, create:\n"
                    "1. A PERSONAL MESSAGE: One very warm appreciation message exactly 1.5 to 2 lines long.\n"
                    "2. 5 COMMENTS: Five short, polite English comments.\n"
                    f"Transcript: {transcript}"
                )
                response = model.generate_content(prompt)
                st.markdown("### ✅ Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}. Please ensure your API Key is correct.")
    else:
        st.warning("Please paste a transcript first!")

# 4. Developed By Section (Animated)
st.markdown('<div class="dev-section">Developed By: SAGOR</div>', unsafe_allow_html=True)

# 5. WhatsApp Button
st.markdown('<a href="https://wa.link/kp3qzu" target="_blank" class="wa-btn">💬 Contact Me on WhatsApp</a>', unsafe_allow_html=True)

# 6. Large Footer
st.markdown('<div class="footer-text">Premium Edition | v2.0 | Advanced Content Generator</div>', unsafe_allow_html=True)
