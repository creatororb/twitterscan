from fastapi import FastAPI
from scanner import scan_tweets

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Twitter scanner is live"}

@app.get("/scan")
def scan(keyword: str, limit: int = 10):
    return scan_tweets(keyword, limit)
