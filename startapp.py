import os

import uvicorn
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
SCHEME = os.environ.get("SCHEME")


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=int(PORT), host=HOST)
