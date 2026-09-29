import streamlit as st


st.title("AI Programming Tutor")

st.write(
    "基于大语言模型的渐进式编程学习与知识诊断系统"
)


question = st.text_area(
    "请输入编程题目"
)


code = st.text_area(
    "请输入你的代码"
)


if st.button("开始 AI 诊断"):
    st.success("代码已提交，等待 AI 分析...")
