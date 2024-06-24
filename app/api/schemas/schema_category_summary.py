from pydantic import BaseModel


class CategorySummary(BaseModel):
    category_name: str
    new_articles_count: int

    class Config:
        from_attributes = True
