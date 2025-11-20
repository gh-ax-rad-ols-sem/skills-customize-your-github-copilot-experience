from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO: Define the Book model using Pydantic BaseModel
# Include fields: id (int), title (str), author (str), year (int), isbn (str)


# TODO: Create an in-memory database (list) with sample books


# TODO: Implement GET /books endpoint
# Should return all books


# TODO: Implement GET /books/{book_id} endpoint
# Should return a single book or 404 if not found


# TODO: Implement POST /books endpoint
# Should create a new book and return it with status 201


# TODO: Implement PUT /books/{book_id} endpoint
# Should update an existing book or return 404 if not found


# TODO: Implement DELETE /books/{book_id} endpoint
# Should delete a book and return status 204, or 404 if not found


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
