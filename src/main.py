import logging
import uvicorn
from fastapi import FastAPI

log = logging.getLogger(__name__)
logging.basicConfig(level="INFO", format="%(levelname)s:%(message)s:%(pathname)s:%(funcName)s:%(lineno)d")

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
