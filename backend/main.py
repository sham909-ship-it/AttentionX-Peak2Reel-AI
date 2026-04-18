from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from backend.services.scorer import score_clip
from backend.services.captions import generate_caption

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    try:
        print("File received:", file.filename)

        chunks = [
            "Consistency beats motivation every single time.",
            "Most students fail because they don’t follow a system.",
            "You don’t need 10 hours, you need the right 2 hours."
        ]

        results = []

        for chunk in chunks:
            try:
                score_data = score_clip(chunk)
            except Exception as e:
                print("Score error:", e)
                score_data = {"score": 80, "label": "Fallback", "reasons": ["Error fallback"]}

            try:
                caption_data = generate_caption(chunk)
            except Exception as e:
                print("Caption error:", e)
                caption_data = {"hook": "Demo hook", "caption": chunk, "hashtags": ["#demo"]}

            results.append({
                "text": chunk,
                "score": score_data,
                "caption": caption_data
            })

        return {"results": results}

    except Exception as e:
        print("BIG ERROR:", e)
        return {"error": str(e)}