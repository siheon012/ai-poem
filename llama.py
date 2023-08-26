import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import CTransformers

llm=CTransformers(
    model="llama-2-7b-chat.ggmlv3.q5_1.bin",
    model_type="llama"
)

st.title('ai poet')


content = st.text_input('write a poem about')


if st.button('requirement'):
    with st.spinner("ing,,,,"):
        result=llm.predict(content + "write a poem about" + content + ":")
        st.write(result)




