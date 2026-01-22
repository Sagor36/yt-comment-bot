import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল API Key বসান
genai.configure(api_key="আপনার_আসল_এপিআই_কি_এখানে_দিন")

# মডেলের নাম আপডেট করে দেখুন
model = genai.GenerativeModel('AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto') 

st.title("YouTube English Comment Generator")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ইংরেজিতে প্রশংসা মূলক কমেন্ট লিখে দেব।")

transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        with st.spinner('AI analysis korche...'):
            try:
                prompt = f"Provide 5 polite, appreciative English YouTube comments based on this transcript: {transcript}"
                response = model.generate_content(prompt)
                st.success("Results:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("Please paste transcript first!")
