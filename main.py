from fastapi import FastAPI
import uvicorn
app = FastAPI()
@app.get('/saludo')
def saludo():
    return {"msg":"Saludos Campers"}
if __name__=="__main__":
    uvicorn.run("main:app",port=8000)
