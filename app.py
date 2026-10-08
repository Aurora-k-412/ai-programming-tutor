import streamlit as st
from services.llm_service import analyze_code

st.title("AI Programming Tutor")

st.write("基于大语言模型的渐进式编程学习与知识诊断系统")

question = st.text_area("请输入编程题目")

code = st.text_area("请输入你的代码",height=200)

if st.button("开始AI诊断"):
    if not question.strip() or not code.strip():
        st.warning("请先输入题目和代码！")

    else:
        result = analyze_code(code)

        st.subheader("AI 诊断结果")

        st.write("**错误类型：**",result["error_type"])

        st.write("**涉及知识点：**",result["knowledge"])

        st.write("**问题分析：**",result["analysis"])

        st.info("💡 Hint 1：" + result["hint"])

