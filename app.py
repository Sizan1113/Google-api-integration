import streamlit as st
from model import gemini_llm
 
st.title("Gemini LLM")
st.subheader("Generate Content with Gemini API LLM")
 
user_input = st.text_area(
    "Enter your prompt.. ",
    placeholder="What is Gemini?"
)
 
 
if st.button("Generate Content"):
    if user_input.strip() == "":
        st.warning("Enter valid prompt!!")
    else:
        with st.spinner("Generating Content"):
            answer = gemini_llm(user_input)
            st.success("Generated Content!")
            st.write(answer)