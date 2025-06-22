def detect_language(code: str) -> str:
    if "def " in code:
        return "Python"
    elif "public static" in code or "class" in code:
        return "Java"
    return "Unknown"
