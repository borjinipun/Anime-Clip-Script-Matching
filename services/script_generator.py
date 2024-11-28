import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(prompt, max_tokens=500):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative anime story writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response["choices"][0]["message"]["content"]
