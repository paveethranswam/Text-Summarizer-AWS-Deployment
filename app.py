from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.inference import InferencePipeline
from main import begin_main


app = FastAPI()

@app.get('/', tags = ['authentication'])
def index():
    return RedirectResponse(url = "/docs")

@app.get('/train', tags=['Training'])
def train():
    try:
        # os.system("python main.py")
        begin_main()
        return Response("Training done")
    except Exception as e:
        return Response("Error ", e)


@app.get('/predict')
def predict(text):
    try:
        infp = InferencePipeline()
        prediction = infp.inference(text)
        return prediction
    
    except Exception as e:
        return Response("Error ", e)
    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8080)










