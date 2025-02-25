
import streamlit as st
from gemini_helper import get_gemini_response

# Page config
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="💬", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .main { background-color: #f4f4f4; }
        .chat-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .response-box {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
        }
        .error-box {
            background-color: #ffcccb;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            font-weight: bold;
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

# UI Design
st.markdown('<h1 style="text-align:center;">💬 Gemini AI Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<h4 style="text-align:center; color:gray;">Ask me Anything!</h4>', unsafe_allow_html=True)

# User Input Area
user_input = st.text_area("👤 You:", "", height=100)
submit = st.button("Send")

if submit and user_input.strip():
    try:
        response = get_gemini_response(user_input)
        st.markdown(f'<div class="response-box">🤖 <b>Gemini:</b> {response}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-box">❌ Error: {e}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
