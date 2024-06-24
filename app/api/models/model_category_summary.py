from sqlalchemy import Column, Integer, String, Date
from db import Base

class CategorySummary(Base):
    __tablename__ = "daily_new_articles_summary"

    category_name = Column(String, primary_key=True)
    new_articles_count = Column(Integer)
