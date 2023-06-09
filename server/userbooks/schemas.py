from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from ninja import Schema
from pydantic import conint

from books.schemas import BookOut


class ShelfIn(Schema):
    name: str


class ShelfOut(ShelfIn):
    id: int


class ShelfBookIn(Schema):
    user_book_id: int


class CurrentlyReadingIn(Schema):
    user_book_id: int
    status: bool


class UserBookIn(Schema):
    book_id: int
    shelves: Optional[List[int]]


class UserBookUpdate(Schema):
    shelves: Optional[List[int]]



class UserBookBase(Schema):
    id: int
    book: BookOut
    is_currently_reading: bool


class UserBookOut(UserBookBase):
    shelves: Optional[List[ShelfOut]]


class ShelfBookOut(UserBookBase):
    shelf_name: str


class CurrentlyReadingBookOut(UserBookOut):
    progress: Optional[Decimal]


class UserBookSessionBase(Schema):
    progress: Optional[Decimal]
    started_at: Optional[datetime]
    finished_at: Optional[datetime]


class UserBookSessionOut(UserBookSessionBase):
    id: int
    progress_updated_at: Optional[datetime]


class UserBookSessionIn(UserBookSessionBase):
    pass


class ReadingProgressIn(Schema):
    user_book_id: int
    progress: conint(ge=0)
