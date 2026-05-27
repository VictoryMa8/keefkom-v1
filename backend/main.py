import os
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()
load_dotenv()

GNEWS_KEY = os.getenv("GNEWS_KEY")

class Article(BaseModel):
    title: str
    publishedAt: str
    url: str
    description: str
    image: str

async def fetch_news(max, country_code): 
    url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country={country_code}&max={max}&apikey={GNEWS_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
@app.get("/news")
async def get_news():
    # Use fetch_news to get 10 articles
    data = await fetch_news(10, 'us')
    # Getting values of "articles" key from response
    return {"articles": data["articles"]}
"""

@app.get("/news/{country_code}", response_model=list[Article])
# Takes country code from url, states that its a str with min & max length of 2
# <...> means its required, no default
# Pattern states that the regex pattern should be this
async def get_news(country_code: str = Path(..., min_length=2, max_length=2, pattern=r"^[a-z]{2}$")):
    data = await fetch_news(10, country_code)
    return data["articles"]