import os
from groq import Groq

# Set Groq API Key
GROQ_API_KEY = "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"

# Function to perform translation using Groq API
def translate_text(sentence, target_language):
    client = Groq(api_key=GROQ_API_KEY)
    
    # Construct the translation prompt
    prompt = f"Translate the following sentence '{sentence}' into {target_language}."
    
    # Make the API call to get the translation
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    # Collect the response chunks
    translated_text = ""
    for chunk in completion:
        translated_text += chunk.choices[0].delta.content or ""
    
    return translated_text
