from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les requêtes de ton navigateur
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Bienvenue sur ton agent Render 🚀"}

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    print("📩 Message reçu :", user_message)

    # Réponse basique (tu pourras la rendre plus intelligente plus tard)
    bot_reply = f"Tu as dit : {user_message}"

    return {"reply": bot_reply}
