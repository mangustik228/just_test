from fastapi import FastAPI


app = FastAPI()

@app.get('/home')
def home():
    return {'status':'ok','page':'home','app':'db'}