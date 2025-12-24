from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_summary(prompt, model="gpt-4", temperature=0.3):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a senior FP&A analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
