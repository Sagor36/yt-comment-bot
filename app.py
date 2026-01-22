import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসাবেন
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="YT Comment AI", page_icon="🎥")
st.title("YouTube English Comment Generator")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ইংরেজিতে প্রশংসা মূলক কমেন্ট লিখে দেব।")

# Input area
transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        with st.spinner('AI is analyzing...'):
            prompt = f"Read this transcript and generate 5 very polite and appreciative YouTube comments in English: {transcript}"
            response = model.generate_content(prompt)
            st.success("Success! Here are your comments:")
            st.write(response.text)
    else:
        st.error("Please paste a transcript first!")
