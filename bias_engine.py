from groq import Groq
import json
import re
from prompts import BIAS_DETECTION_PROMPT

# GROQ API KEY
API_KEY = "paste your api key here"

client = Groq(api_key=API_KEY)

def analyze_bias(article_text):
    prompt = BIAS_DETECTION_PROMPT.format(article_text=article_text)

    print("Sending request to Groq...")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024
    )

    response_text = response.choices[0].message.content

    print("RAW GROQ RESPONSE:")
    print(response_text)
    print("---------------------")

    try:
        result = json.loads(response_text)
        return result
    except:
        pass

    try:
        match = re.search(r"```json(.*?)```", response_text, re.DOTALL)
        if match:
            return json.loads(match.group(1).strip())
    except:
        pass

    try:
        match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if match:
            return json.loads(match.group(0).strip())
    except:
        pass

    return {
        "bias_type": "Error parsing",
        "tone": "Error parsing",
        "framing": "Error parsing",
        "missing_perspectives": "Error parsing",
        "loaded_language": [],
        "bias_score": 0,
        "summary": response_text
    }