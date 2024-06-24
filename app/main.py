import os
import sys
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from api.routes.route_category_summary import router as category_summary_router


load_dotenv()


app = FastAPI()
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
app.include_router(category_summary_router, prefix="/api")

# Código adicional para la configuración y arranque del servidor
