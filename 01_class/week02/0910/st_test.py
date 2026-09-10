# ChatGPT와 유사한 앱 개발방법
# https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps


import streamlit as st
import random
import time

st.title("Heeyeong's Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history an app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
# := 연산자를 사용하여 사용자의 입력을 prompt변수에 할당하고, 같은 줄에 입력했는지 확인
if prompt := st.chat_input("Say something"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add uer message to chat history
    # ->a ppend() 사용자의 입력이나 챗봇의 응답을 메시지 리스트에 누적할 때 사용
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulater
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display bot response in chat message container
with st.chat_message("bot"):
    response = st.write_stream(response_generator())
# Add bot response to chat history
st.session_state.messages.append({"role": "bot", "content": response})