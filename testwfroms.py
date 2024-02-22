from pymongo import MongoClient
from fastapi import FastAPI,Form,Request#,APIRouter
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import uvicorn
#from pydantic import BaseModel

app=FastAPI()
tempts=Jinja2Templates(directory="templates")
conn=MongoClient("localhost",27017)

db=conn.testpymongo
coln=db['userdet']

class Datas():
    nms:str
    educns:str

# def savecandid(dct):
#     print(dct)
#     id=coln._insert_one(dct).inserted_id
#     print("conts added " + str(id))
   #userdet=coln.find({})

@app.post("/savecandid",response_model=None)
def savecandid(request:Request, cntnt:str=Form(),educn:str=Form()):
    #nm:str=Form(...),educn:str=Form(...)
    print('post method called...')
    nms=cntnt#:str=Form(...)
    educns=educn #:str=Form(...)
    print(nms)
    print(educns)
    dt=Datas(nms=cntnt,educns=educn)
    print(dict(dt))
    #savecandid(dt.dict())
    id=coln.insert_one(dict(dt)).inserted_id
    print("conts added " + str(id))
    userdet=coln.find({})
    return tempts.TemplateResponse("index.html",{"request":req,"candid_list":userdet})



@app.get("/")
async def index(req:Request):
    return tempts.TemplateResponse("index.html",context={"request":req})


if (__name__)=="__main__":
    uvicorn.run("testwfroms:app",host="127.0.0.1",port=8081,reload=True)






