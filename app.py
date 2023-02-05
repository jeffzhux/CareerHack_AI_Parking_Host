from fastapi import FastAPI, APIRouter
import uvicorn

from router import login, home

app = FastAPI()
app.include_router(login.router)
app.include_router(home.router)

if __name__ == "__main__":
    uvicorn.run(app, )
