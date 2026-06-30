import streamlit as st
from chatbot import HealthcareChatbot

st.title("AI-Powered Healthcare Chatbot")

chatbot = HealthcareChatbot()

user_input = st.text_input("How can I assist you today? ")
if st.button("Submit"):
    st.write(f"User: {user_input}")
    response = chatbot.get_response(user_input)
    st.write(f"Healthcare Assistant: {response}")
