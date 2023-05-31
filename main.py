from fastapi import FastAPI
from pydantic import BaseModel

import utils

app = FastAPI()


class Picture(BaseModel):
    data: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/predict/")
async def recognize_mushroom(picture: Picture):
    # image = utils.decode_img(picture.data)
    prediction, location = utils.predict(None, None)
    print(prediction)
    return {
        "name": prediction,
        "location": location
    }


@app.get("/locations/sample/{name}")
async def get_mushrooms_sample(name: str, num: int = 10):
    return utils.get_samples(name, num)
