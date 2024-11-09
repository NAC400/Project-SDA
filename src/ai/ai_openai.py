# src/ai_helper.py
import openai

openai.api_key = 'your_openai_api_key'

def ask_ai_for_code(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def ai_generate_code(command):
    prompt = f"Write a Python function to {command}"
    code = ask_ai_for_code(prompt)
    return code