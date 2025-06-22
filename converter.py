from google import genai

def convert_code(function_code, from_lang, to_lang):
    prompt = f"Convert the following {from_lang} function to {to_lang}. Don't change function signature.\n\n{function_code}"
    client = genai.Client(api_key='GEMINI_API_KEY')
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    return response.text
