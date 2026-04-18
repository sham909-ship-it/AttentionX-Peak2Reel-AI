from google import genai

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

def generate_caption(text, platform="instagram", audience="student"):
    prompt = f"""
    You are a viral content creator for {audience} audience in India.

    Convert this into:
    1. Hook (max 10 words)
    2. Caption (2 lines)
    3. 5 hashtags

    Platform: {platform}

    Text:
    "{text}"

    Return ONLY JSON:
    {{
      "hook": "...",
      "caption": "...",
      "hashtags": ["#tag1","#tag2"]
    }}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text