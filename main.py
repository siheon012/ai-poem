from dotenv import load_dotenv #playgrond
load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

#from langchain.llms import OpenAI #OpenAI에서 langchain.llms 를 사용 이 앱은 predict 괄호 안 단어를 뒤를
                                  # 예측하여 말을 이어줌
#llm=OpenAI()
#result =llm.perdict("hi")
#print(result)

 #이거는 predict 안 단어를 입력하면, 그에 맞는 대화 문장이 
                                             #출력된다
chat_model=ChatOpenAI()
st.title('인공지능 시인')


content = st.text_input('시의 주제를 입력해주세요')


if st.button('시 작성 요청'):
    result=chat_model.predict(content + "에 대한 시를 써줘")
    st.write(result)




