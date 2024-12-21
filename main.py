import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Create prompt template for code explanation
code_explanation_template = PromptTemplate(
    input_variables=["code"],
    template="""You are an expert programmer and teacher. Please explain the following code in detail, 
    covering these aspects:
    1. Overall purpose and functionality
    2. Breakdown of key components and their roles
    3. Important programming concepts used
    4. Potential improvements or best practices to consider

    Code to explain:
    {code}

    Please provide a clear and comprehensive explanation."""
)

# Create LangChain chain
code_chain = LLMChain(
    llm=llm,
    prompt=code_explanation_template,
    verbose=True
)

# Streamlit UI
st.title("🤖 AI Code Explainer")
st.markdown("""
This app uses AI to provide detailed explanations of code snippets. 
Simply paste your code below and get a comprehensive explanation!
""")

# Code input
code_input = st.text_area("Enter your code here:", height=300)

if st.button("Explain Code"):
    if code_input:
        with st.spinner("Analyzing code..."):
            try:
                # Get explanation
                explanation = code_chain.run(code_input)
                
                # Display explanation
                st.markdown("### 📝 Code Explanation")
                st.markdown(explanation)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some code to explain.")
