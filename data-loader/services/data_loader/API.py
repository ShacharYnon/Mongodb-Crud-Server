from fastapi import FastAPI ,HTTPException
from services.data_loader.DAL import DAL


app = FastAPI(title="Document Management API" ,version="1.0.0")
dal = DAL()

class API:
    pass