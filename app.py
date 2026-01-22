import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল API Key বসান
genai.configure(api_key="AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto")

# লেটেস্ট মডেল ব্যবহার করা হয়েছে যা দ্রুত কাজ করে
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("YouTube English Comment Generator 🎥")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ইংরেজিতে প্রশংসা মূলক কমেন্ট লিখে দেব।")

# Input area
transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        # স্ট্যাটাস মেসেজ
        with st.status("AI analysis korche...", expanded=True) as status:
            try:
                prompt = f"Based on this YouTube transcript, generate 5 polite and appreciative English comments: {transcript}"
                response = model.generate_content(prompt)
                
                st.subheader("✅ Results:")
                st.write(response.text)
                status.update(label="Analysis Complete!", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Error: {e}")
                status.update(label="Error occurred!", state="error")
    else:
        st.warning("Please paste a transcript first!")
