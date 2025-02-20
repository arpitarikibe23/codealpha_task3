import streamlit as st
import google.generativeai as genai

# Configure Google AI API
API_KEY = "AIzaSyAWsmiTKVYlrBguTNruGd1AT8SPeaeHTBk"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Function to get AI response
def get_gemini_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text.strip() if response and response.text else "Sorry, I couldn't understand that."

# Streamlit UI
st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    bot_response = get_gemini_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.write(bot_response)
