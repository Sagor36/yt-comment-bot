import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key টি বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন
def get_available_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            return m.name
    return None

available_model_name = get_available_model()

st.set_page_config(page_title="YT Comment AI", page_icon="🎥")
st.title("YouTube English Comment Generator 🎥")

transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        if available_model_name:
            with st.status(f"Using {available_model_name}...", expanded=True) as status:
                try:
                    model = genai.GenerativeModel(available_model_name)
                    prompt = f"Provide 5 polite, appreciative English comments for this YouTube transcript: {transcript}"
                    response = model.generate_content(prompt)
                    
                    st.subheader("✅ Recommended Comments:")
                    st.write(response.text)
                    status.update(label="Success!", state="complete", expanded=False)
                except Exception as e:
                    st.error(f"Error: {e}")
                    status.update(label="Failed!", state="error")
        else:
            st.error("No compatible Gemini model found for this API Key.")
    else:
        st.warning("Please paste a transcript first!")
