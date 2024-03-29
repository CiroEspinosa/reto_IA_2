from openai import OpenAI
import streamlit as st


client = OpenAI(

)

EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_EMBEDDING_ENGINE = 'mondongodb'
DIMENSION = 1536
GPT_MODEL = 'gpt-3.5-turbo-16k'
GPT_CHAT_ENGINE = "gepeto"
# GPT_MODEL = 'gpt-4'
# GPT_CHAT_ENGINE = "dictador"


st.title("Chatbot")

if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]

for msg in st.session_state["messages"]:
  st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
  st.session_state["messages"].append({"role": "user", "content": user_input})
  st.chat_message("user").write(user_input)

  response = client.completions.create(
        model=GPT_MODEL,
        prompt=st.session_state["messages"]
    )
  
  responseMessage = response.choices[0].message.content
  st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
  st.chat_message("assistant").write(responseMessage)
