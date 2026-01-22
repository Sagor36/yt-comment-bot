import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"
genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন যাতে এরর না আসে
def get_model():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        flash_models = [m for m in models if "flash" in m]
        return genai.GenerativeModel(flash_models[0] if flash_models else models[0])
    except:
        return genai.GenerativeModel('gemini-1.5-flash')

# Page Setup
st.set_page_config(page_title="YT AI Studio Pro", page_icon="🚀", layout="centered")

# Custom UI Design with Premium Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    
    body { background-color: #0e1117; font-family: 'Poppins', sans-serif; }
    .stApp { background-color: #0e1117; }
    
    /* exclusive Title Border */
    .exclusive-header {
        border: 4px solid #FF3131;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        background: rgba(255, 49, 49, 0.1);
        font-size: 32px;
        font-weight: bold;
        color: #FF3131;
        margin-bottom: 30px;
        box-shadow: 0 0 25px rgba(255, 49, 49, 0.4);
        text-transform: uppercase;
    }

    /* Large Input Label */
    .input-label {
        font-size: 26px;
        font-weight: bold;
        color: #00FFCC; /* উজ্জ্বল নিওন কালার */
        margin-bottom: 15px;
        display: block;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }

    /* Action Button Styling */
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 24px !important;
        font-weight: bold;
        color: white;
        background: linear-gradient(90deg, #FF3131, #FF914D);
        border: 2px solid #ffffff;
        border-radius: 15px;
        transition: 0.5s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 49, 49, 0.6);
    }

    /* Result Section with Neon Border */
    .result-card {
        border: 3px solid #00FFCC;
        padding: 25px;
        border-radius: 15px;
        background: rgba(0, 255, 204, 0.05);
        margin-top: 30px;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
        color: #ffffff;
        animation: fadeIn 1.5s ease-in-out;
    }
    .result-title {
        color: #00FFCC;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
    }

    /* Developed By Animated Glow Section */
    @keyframes glow-blue {
        0% { box-shadow: 0 0 10px #00B4DB; border-color: #00B4DB; }
        50% { box-shadow: 0 0 40px #00FBFF; border-color: #00FBFF; }
        100% { box-shadow: 0 0 10px #00B4DB; border-color: #00B4DB; }
    }
    .dev-section {
        border: 6px solid #00B4DB;
        padding: 25px;
        border-radius: 60px;
        text-align: center;
        margin-top: 50px;
        font-size: 40px;
        font-weight: 800;
        color: #ffffff;
        background: rgba(0, 180, 219, 0.1);
        animation: glow-blue 2.5s infinite ease-in-out;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
    }

    /* WhatsApp Gradient Button */
    .wa-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(90deg, #25D366, #128C7E);
        color: white !important;
        padding: 18px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
        transition: 0.3s;
        box-shadow: 0 5px 20px rgba(37, 211, 102, 0.4);
    }
    .wa-btn:hover { transform: scale(1.02); box-shadow: 0 8px 25px rgba(37, 211, 102, 0.6); }

    /* Bottom Info Text */
    .version-text {
        font-size: 20px;
        color: #555;
        text-align: center;
        margin-top: 40px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Exclusive Header
st.markdown('<div class="exclusive-header">🎥 YOUTUBE MESSAGE & COMMENT AI</div>', unsafe_allow_html=True)

# 2. Input Label & Text Area
st.markdown('<span class="input-label">Paste Video Transcript Below:</span>', unsafe_allow_html=True)
transcript = st.text_area("", height=220, placeholder="ভিডিওর ট্রান্সক্রিপ্ট এখানে পেস্ট করুন...", key="main_input")

# 3. Action Button
if st.button("🚀 GENERATE MESSAGE AND COMMENT"):
    if transcript:
        with st.spinner('🤖 AI বিশ্লেষণ করছে...'):
            try:
                model = get_model()
                # Prompt for short message and comments
                prompt = (
                    "Using the following transcript, create:\n"
                    "1. A PERSONAL MESSAGE: One warm appreciation message strictly 1.5 to 2 lines long in English.\n"
                    "2. 5 COMMENTS: Five short, polite English comments.\n"
                    f"Transcript: {transcript}"
                )
                response = model.generate_content(prompt)
                
                # Result with Neon Border
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">✅ Generated Content:</div>
                    <div style="font-size: 18px; line-height: 1.6; color: #E0E0E0; font-weight: 500;">
                        {response.text.replace('**', '<b>').replace('\n', '<br>')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("আগে ট্রান্সক্রিপ্ট পেস্ট করুন!")

# 4. Animated Developer Section
st.markdown('<div class="dev-section">Developed By: SAGOR</div>', unsafe_allow_html=True)

# 5. WhatsApp Button
st.markdown('<a href="https://wa.link/kp3qzu" target="_blank" class="wa-btn">💬 Contact Me on WhatsApp</a>', unsafe_allow_html=True)

# 6. Large Styled Footer
st.markdown('<div class="version-text">PREMIUM EDITION | V2.0 | ADVANCED AI ENGINE</div>', unsafe_allow_html=True)
