import sys
import os
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from api.schemas.schema_category_summary import CategorySummary
from db.db import get_db


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_model=List[CategorySummary],response_class=HTMLResponse)
def get_category_summary(request: Request, db: Session = Depends(get_db)):
    try:
        query = text("""
            SELECT category_name, new_articles_count
            FROM daily_new_articles_summary ORDER BY new_articles_count DESC LIMIT 6;
        """)
        result = db.execute(query)
        summaries = result.mappings().all()  # Use mappings() to get a list of dictionaries

        return templates.TemplateResponse("index.html", {"request": request, "summaries": summaries})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
