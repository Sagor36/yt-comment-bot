import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key বসান
# Google AI Studio থেকে পাওয়া কি-টি ডাবল কোটেশনের ভেতর দিন
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# আমরা এখানে 'gemini-pro' ব্যবহার করছি কারণ এটি সব কি-তে ডিফল্টভাবে থাকে
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="YT Comment AI", layout="centered")
st.title("YouTube English Comment Generator 🎥")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ইংরেজিতে প্রশংসা মূলক কমেন্ট লিখে দেব।")

transcript = st.text_area("Paste Transcript Here:", height=250)

if st.button("Generate English Comments"):
    if transcript:
        with st.status("AI analysis korche...") as status:
            try:
                # প্রম্পটটি আরও শক্তিশালী করা হয়েছে
                prompt = f"Please read the following transcript and generate 5 polite, creative, and appreciative YouTube comments in English based on the content: \n\n{transcript}"
                
                response = model.generate_content(prompt)
                
                st.subheader("✅ Results:")
                st.write(response.text)
                status.update(label="Success!", state="complete")
            except Exception as e:
                st.error(f"Error occurred: {e}")
                status.update(label="Failed!", state="error")
    else:
        st.warning("Please paste a transcript first!")
