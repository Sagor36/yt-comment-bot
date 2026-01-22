import streamlit as st
import google.generativeai as genai

# এখানে আপনার আসল Gemini API Key টি বসান
API_KEY = "AIzaSyDENWVUBpXQfNmpTAE8qBt3g_D6-Qb1Oto"

genai.configure(api_key=API_KEY)

# সঠিক মডেল খুঁজে বের করার ফাংশন যাতে এরর না আসে
def get_working_model():
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # প্রথম পছন্দের মডেল gemini-1.5-flash, না থাকলে অন্যটি নিবে
    if 'models/gemini-1.5-flash' in available_models:
        return genai.GenerativeModel('gemini-1.5-flash')
    elif 'models/gemini-pro' in available_models:
        return genai.GenerativeModel('gemini-pro')
    else:
        return genai.GenerativeModel(available_models[0])

st.set_page_config(page_title="YT Feedback AI", page_icon="🎥", layout="wide")

st.title("🎥 YouTube Appreciation & Comment Generator")
st.write("যেকোনো ভাষার ট্রান্সক্রিপ্ট দিন, আমি ভিডিওর বিষয়বস্তু অনুযায়ী প্রশংসা মূলক মেসেজ এবং কমেন্ট লিখে দেব।")

# ইনপুট এরিয়া
transcript = st.text_area("ভিডিওর ট্রান্সক্রিপ্ট এখানে পেস্ট করুন:", height=300)

if st.button("Generate Appreciation Content"):
    if transcript:
        with st.status("AI ভিডিওর বিষয়বস্তু বিশ্লেষণ করছে...", expanded=True) as status:
            try:
                model = get_working_model()
                
                # প্রম্পটটি আপডেট করা হয়েছে পার্সোনাল মেসেজ এবং কমেন্ট পাওয়ার জন্য
                prompt = (
                    "Based on the YouTube transcript provided, act as an appreciative viewer and generate:\n\n"
                    "1. A PERSONAL APPRECIATION MESSAGE: A warm 3-4 sentence paragraph thanking the creator. "
                    "Mention specific points from the transcript to make it sound real and thoughtful.\n"
                    "2. 5 ENGAGING COMMENTS: 5 distinct, polite, and encouraging English comments for the video.\n\n"
                    "All output must be in English. Keep the tone natural, helpful, and friendly.\n\n"
                    f"Transcript:\n{transcript}"
                )
                
                response = model.generate_content(prompt)
                
                st.success("✅ আপনার জন্য কন্টেন্ট তৈরি হয়েছে:")
                st.markdown("---")
                # ফলাফলটি সুন্দরভাবে দেখানোর জন্য
                st.markdown(response.text)
                
                status.update(label="Success! Content Generated.", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Error occurred: {e}")
                status.update(label="Failed!", state="error")
    else:
        st.warning("দয়া করে আগে ট্রান্সক্রিপ্ট পেস্ট করুন!")

# ফুটার
st.markdown("---")
st.caption("Powered by SAGOR DEVOLOPER | Optimized for Sagor36")
