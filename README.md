# Code Converter

A web application to extract and convert functions between Python and Java using AI (Gemini API).  
Built with [Streamlit](https://streamlit.io/) for an interactive UI.

---

## Features

- **Upload** a Python (`.py`) or Java (`.java`) file.
- **Extract** a specific function/method by name.
- **Convert** the extracted function between Python and Java using Gemini AI.
- **Automatic language detection** for uploaded code.

---

## Project Structure

```
code_converter/
│
├── app.py           # Streamlit web app (main entry point)
├── converter.py     # Handles code conversion using Gemini API
├── extractor.py     # Extracts functions from Python/Java code
├── utils.py         # Utility for language detection
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
└── ...
```

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone [https://github.com/aman-cpu/Code_Converter](https://github.com/aman-cpu/Code_Converter.git)
```

### 2. Create a Python virtual environment

```bash
python -m venv venv
cd venv
```

### 3. Activate the virtual environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. How to Run

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser.  
Upload a `.py` or `.java` file, enter the function name, select the target language, and click "Convert Function".

---

## Notes

- **API Key:**  
  The code conversion uses Gemini AI via the `google-genai` package.  
  Make sure to set your API key in `converter.py` (currently hardcoded).

- **Supported Languages:**  
  - Python (function extraction via AST)
  - Java (function extraction via regex heuristic)

- **Limitations:**  
  - Java extraction uses a regex-based approach and may not handle all edge cases.
  - Only function-level conversion is supported.
  - The conversion quality depends on the Gemini model.

---

## Dependencies

All dependencies are listed in `requirements.txt`.  
Key packages:
- `streamlit`
- `google-genai`
- `altair`, `pandas`, `numpy` (for Streamlit and data handling)

---
