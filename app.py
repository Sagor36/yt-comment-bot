import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key টি বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# সঠিক এবং এভেইলঅ্যাবল মডেল খুঁজে বের করার ফাংশন
def get_model():
    try:
        # gemini-1.5-flash সবচেয়ে দ্রুত এবং মেসেজ তৈরিতে ভালো
        return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="YT Feedback AI", page_icon="🎥", layout="wide")

st.title("🎥 YouTube Appreciation Message & Comment Generator")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ভিডিওর বিষয়বস্তু অনুযায়ী সুন্দর ইংরেজি মেসেজ এবং কমেন্ট লিখে দেব।")

# ইনপুট সেকশন
transcript = st.text_area("ভিডিওর ট্রান্সক্রিপ্ট এখানে পেস্ট করুন:", height=300)

if st.button("Generate Appreciation Feedback"):
    if transcript:
        with st.status("AI ভিডিওর বিষয়বস্তু বিশ্লেষণ করছে...", expanded=True) as status:
            try:
                model = get_model()
                
                # প্রম্পটটি আপডেট করা হয়েছে যাতে মেসেজ এবং কমেন্ট আলাদাভাবে দেয়
                prompt = (
                    "Act as a regular YouTube viewer who just watched a video. "
                    "Based on the transcript provided, generate two things in English:\n\n"
                    "1. A PERSONAL APPRECIATION MESSAGE: Write a warm, 3-4 sentence message thanking the creator "
                    "for specific value they provided in this video (based on the transcript).\n"
                    "2. 5 SHORT COMMENTS: Write 5 distinct, polite, and engaging YouTube comments.\n\n"
                    "Ensure the tone is natural, human-like, and very encouraging.\n\n"
                    f"Transcript:\n{transcript}"
                )
                
                response = model.generate_content(prompt)
                
                st.success("✅ আপনার জন্য ফিডব্যাক তৈরি হয়েছে:")
                st.markdown("---")
                st.write(response.text)
                
                status.update(label="Success! Feedback generated.", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Error occurred: {e}")
                status.update(label="Failed!", state="error")
    else:
        st.warning("দয়া করে আগে ট্রান্সক্রিপ্ট পেস্ট করুন!")

# ফুটার
st.markdown("---")
st.caption("Powered by Sagor Devoloper | Designed for Sagor36")
