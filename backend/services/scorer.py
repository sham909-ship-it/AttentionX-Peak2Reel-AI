from google import genai

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

def score_clip(text):
    prompt = f"""
    You are an expert in viral content for Indian audiences.

    Analyze this:
    "{text}"

    Give:
    1. Score (1-100)
    2. Label (Low/Medium/High/Viral)
    3. 3 short reasons

    Return ONLY JSON like:
    {{
      "score": 85,
      "label": "High",
      "reasons": ["reason1", "reason2", "reason3"]
    }}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text