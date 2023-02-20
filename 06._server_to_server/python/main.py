from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()


@app.get("/date")
def get_date():
    return datetime.now()


@app.get("/datefromexpress")
def get_date_from_express():
    response = requests.get("http://127.0.0.1:8080/date")
    date = response.json()
    return date


@app.get("/dateengrok")
def _():
    response = requests.get("https://40ae-195-249-146-101.eu.ngrok.io/date")
    date = response.json()
    return date
