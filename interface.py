import streamlit as st
# Refer analysis.py file
from analysis import analyze_resume

st.set_page_config(page_title="CV Analyzer")
st.title("RESUME ANALYZER USING AI 🤖🧠🇦🇮👾")

st.subheader('''This page helps you to compare your resume with the given Job description.''')

st.sidebar.subheader('Drop Your resume here')
pdf_doc=st.sidebar.file_uploader("Click here to browse",type=['pdf'])

st.sidebar.markdown('Designed by Kiran u')
st.sidebar.markdown("LinkedIn : 'https://www.linkedin.com/in/kiran-u-471818325/'")
st.sidebar.markdown("Github : 'https://github.com/KIRAN4003'")

job_des=st.text_area('Enter the Job description here 👉',max_chars=10000)

submit=st.button('Generate Score 📊')

if submit:
    with st.spinner('Getting Results...'):
        analyze_resume(pdf_doc,job_des)
        