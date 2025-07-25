import openai
from translation_module import translate

openai.api_key = "your_openai_api_key"

def get_gpt_clarification(user_input, lang="en"):
    translated_input = translate(user_input, lang, "en")

    prompt = f"""
You are a medical assistant. The user says: "{translated_input}"
Ask a few follow-up questions to clarify the symptoms:
- Duration
- Severity
- Associated issues like fever, vomiting, etc.
End with: "Please consult a doctor for further guidance."
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a friendly medical assistant offering safe health clarifications."},
            {"role": "user", "content": prompt}
        ]
    )

    english_response = response.choices[0].message['content']
    return translate(english_response, "en", lang)
