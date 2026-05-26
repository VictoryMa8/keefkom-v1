import os
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

GNEWS_KEY = os.getenv("GNEWS_KEY")

async def fetch_news(max):
    url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=us&max={max}&apikey={GNEWS_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/news")
async def get_news():
    data = await fetch_news(10)
    # Getting values of "articles" key from response
    return {"articles": data["articles"]}