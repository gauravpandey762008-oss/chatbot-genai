import os, requests

# Apni free key yahan paste karo (aistudio.google.com se milegi), quotes ke andar:
API_KEY = os.getenv("GEMINI_API_KEY") or "PASTE_YOUR_KEY_HERE"
MODEL = "gemini-2.0-flash"   # error aaye to AI Studio me naya model name dekh ke badal do

def ask_ai(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    r = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]})
    data = r.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "Error: " + str(data)
