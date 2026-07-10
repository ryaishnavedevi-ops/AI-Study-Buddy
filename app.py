import streamlit as st
import google.generativeai as genai

import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Configure Gemini API

model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="AI Learning Buddy-Yaishnave", page_icon="🎓🎓")
st.title("🎓🎓 AI Learning Buddy-Yaishnave")
topic = st.text_input("Enter a Topic")
option = st.selectbox(
"Choose Activity",
[
"Explain Concept",
"Real-Life Example",
"Generate Quiz",
"Ask Anything"
]
)
if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        try:
            with st.spinner("Generating response..."):
                response = model.generate_content(prompt)

            st.write(response.text)

        except Exception as e:
            if "429" in str(e) or "ResourceExhausted" in str(e):
                st.warning("🚦 Gemini API is busy. Please wait about a minute and try again.")
            else:
                st.error(f"Error: {e}")
