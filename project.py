from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()


class Bookstore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str


@app.post("/books")
def create_book(
    state: Bookstore,
    db: Session = Depends(get_db)
):
    new_book = model.Book(
        id=state.id,
        title=state.title,
        author=state.author,
        publish_date=state.publish_date
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@app.get("/books")
def get_book(db:Session=Depends(get_db)):
    books=db.query(model.Book).all()
    return books