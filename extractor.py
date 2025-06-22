import ast
import re

def extract_function(code, function_name, language):
    if language.lower() == "python":
        try:
            tree = ast.parse(code)
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    return ast.unparse(node)
        except Exception as e:
            print(f"Error parsing Python code: {e}")
            return None

    elif language.lower() == "java":
        # Regex to find method definitions (basic heuristic)
        pattern = rf"(public|private|protected)?\s*(static)?\s*[\w<>\[\]]+\s+{function_name}\s*\([^)]*\)\s*\{{"
        matches = list(re.finditer(pattern, code))

        if matches:
            start = matches[0].start()
            # Now match braces to extract the function block
            brace_count = 0
            in_func = False
            end = start

            for i in range(start, len(code)):
                if code[i] == '{':
                    brace_count += 1
                    in_func = True
                elif code[i] == '}':
                    brace_count -= 1
                if in_func and brace_count == 0:
                    end = i + 1
                    break
            return code[start:end].strip()

    return None
