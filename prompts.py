BIAS_DETECTION_PROMPT = """
Analyze the following news article for bias. You must respond ONLY with a valid JSON object. No explanation, no extra text, just the JSON.

The JSON must have exactly these fields:
{{
  "bias_type": "write the type of bias here",
  "tone": "write the tone here",
  "framing": "write how the story is framed here",
  "missing_perspectives": "write what viewpoints are missing here",
  "loaded_language": ["word1", "word2", "word3"],
  "bias_score": 5,
  "summary": "write a short summary of the bias found here"
}}

Article to analyze:
{article_text}

Remember: Reply with ONLY the JSON. Nothing before it. Nothing after it.
"""

