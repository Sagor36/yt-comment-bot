import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসান
# API Key-টি অবশ্যই ডাবল কোটেশন (" ") এর ভেতর দিবেন
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# আমরা এখানে 'gemini-1.5-flash-latest' ব্যবহার করছি যা সবচেয়ে নতুন এবং দ্রুত
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="YT Comment AI", page_icon="🎥")
st.title("YouTube English Comment Generator 🎥")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ইংরেজিতে প্রশংসা মূলক কমেন্ট লিখে দেব।")

# Input area
transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        with st.status("AI analysis korche...", expanded=True) as status:
            try:
                # প্রম্পটটি আপডেট করা হয়েছে যাতে যেকোনো ভাষার ট্রান্সক্রিপ্ট বুঝুক
                prompt = (
                    "Read the following YouTube video transcript. Regardless of the language of the transcript, "
                    "generate 5 polite, creative, and appreciative comments in English that I can post on the video. "
                    f"\n\nTranscript:\n{transcript}"
                )
                
                response = model.generate_content(prompt)
                
                st.subheader("✅ Recommended Comments (English):")
                st.write(response.text)
                status.update(label="Success!", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Error: {e}")
                status.update(label="Failed!", state="error")
    else:
        st.warning("Please paste a transcript first!")
