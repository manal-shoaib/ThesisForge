import streamlit as st
from groq import Groq

st.title("Thesis AI Assistant")

# Input for your Groq API key
api_key = st.text_input("Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)
    
    # Text box for chatting
    user_input = st.text_input("Type something to the AI:")
    
    if user_input:
        # Send message to Groq's model
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile",
        )
        
        # Display the response
        st.write("AI Response:")
        st.write(chat_completion.choices[0].message.content)