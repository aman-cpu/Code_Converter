# code_converter/app.py

import streamlit as st
from extractor import extract_function
from converter import convert_code
from utils import detect_language

st.set_page_config(page_title="Code Converter", layout="wide")
st.title("🔄 Code Converter - Python ↔ Java")

# Sidebar or top area for inputs
uploaded_file = st.file_uploader(
    "📂 Upload your code file (.py or .java)", type=["py", "java"]
)
function_name = st.text_input("🧠 Enter the function name to convert")
target_language = st.selectbox("🎯 Select target language", ["Java", "Python"])

# Add submit button
if st.button("🚀 Convert Function"):
    if not uploaded_file or not function_name or not target_language:
        st.warning(
            "Please upload a file, enter a function name, and select a target language."
        )
    else:
        code = uploaded_file.read().decode("utf-8")

        # Detect input language (optional bonus feature)
        detected_language = detect_language(code)
        st.write(f"🔍 Detected input language: `{detected_language}`")

        # Extract the function
        function_code = extract_function(code, function_name, detected_language)

        if function_code:
            st.subheader("📌 Extracted Function")
            st.code(function_code, language=detected_language.lower())

            # Convert the function
            converted_code = convert_code(
                function_code, detected_language, target_language
            )

            st.subheader("🚀 Converted Function")
            st.code(converted_code, language=target_language.lower())

            st.success(f"✅ Conversion Done...")
        else:
            st.error("❌ Function not found in the uploaded file.")
