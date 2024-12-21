# AI Code Explainer

An AI-powered application that provides detailed explanations of code snippets using LangChain and Llama 2 (via Groq Cloud).

## Features

- Paste any code snippet and get a detailed explanation
- Covers purpose, functionality, key components, and best practices
- Modern and user-friendly interface built with Streamlit
- Powered by Llama 2 70B model through Groq Cloud

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Running the Application

Run the Streamlit app using:
```bash
streamlit run main.py
```

The application will open in your default web browser.

## Usage

1. Enter or paste your code in the text area
2. Click the "Explain Code" button
3. Wait for the AI to analyze and explain your code
4. Review the detailed explanation provided

## Requirements

- Python 3.8+
- Groq API key
- Internet connection

## Note

Make sure to keep your API key secure and never commit it to version control. 