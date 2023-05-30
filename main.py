import os
from fastapi import FastAPI
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

app = FastAPI()

@app.get('/home')
def home():
    logger.info(f'{os.getenv("hello")}')
    return {'status':'ok','page':'home','app':'db'}