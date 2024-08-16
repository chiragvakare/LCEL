import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": f"{input_text}"
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
    
    response_json = response.json()
    output_text = response_json.get("output", "No response output available")
    
    return output_text

## Streamlit app
st.title("LLM Application Using LCEL")

# Select language
language = st.selectbox(
    "Select the language to convert to",
    [
        "French", "Spanish", "German", "Hindi", "Chinese", "Japanese",
        "Russian", "Portuguese", "Italian", "Korean"
    ]
)

input_text = st.text_input("Enter the text you want to convert")

if input_text:
    st.write(get_groq_response(input_text, language))
