import os
from google import genai
import streamlit as st

# Page layout
st.title("🤖 My Simple AI Assistant")
st.write("Type a prompt below to chat with Gemini!")

# Securely grab the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Missing GEMINI_API_KEY! Please set it in app settings.")
else:
    # Initialize Google GenAI client
    client = genai.Client(api_key=api_key)

    # Input box for user query
    user_input = st.text_input("Ask anything:", "Tell me a fun fact about space.")

    # Button to submit
    if st.button("Generate Answer"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_input,
                )
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
