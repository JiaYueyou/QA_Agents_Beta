import streamlit as st
from main import multi_agent_answer

st.title("多 Agent 企业知识库（LangChain 0.3.27）")

query = st.text_input("请输入你的问题：")

if st.button("查询"):
    st.write(multi_agent_answer(query))
