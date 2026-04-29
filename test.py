from groq import Groq

API_KEY = "paste your api key here"

client = Groq(api_key=API_KEY)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

print("SUCCESS! Groq said:")
print(response.choices[0].message.content)