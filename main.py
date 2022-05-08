from http.client import responses
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Success!"}

@app.get("/about")
async def root():
    return {"message":"Successfully navigated to /about!"}

@app.get("/contact")
async def root():
    return {"message":"Successfully navigated to /contact!"}

@app.get("/home")
async def root():
    return {"message":"Successfully navigated to /home!"}


# /home/image will give you image
@app.get(
    "/home/image",
    response_class= FileResponse
    )
async def home():
    return "src/img/image.png"