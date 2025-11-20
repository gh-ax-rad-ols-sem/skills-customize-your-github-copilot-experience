# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using FastAPI framework. You'll create a simple Book Management API that supports CRUD (Create, Read, Update, Delete) operations with proper HTTP methods and status codes.

## 📝 Tasks

### 🛠️	Create Basic API Structure

#### Description
Set up a FastAPI application with basic endpoints to manage a collection of books. Each book should have an id, title, author, year, and ISBN.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Define a Book model using Pydantic BaseModel with appropriate field types
- Create an in-memory list to store books as a simple database
- Include at least 3 sample books in the initial data
- Run the application using uvicorn when executed


### 🛠️	Implement CRUD Endpoints

#### Description
Create REST API endpoints that allow users to perform all CRUD operations on the book collection.

#### Requirements
Completed program should:

- `GET /books` - Return a list of all books
- `GET /books/{book_id}` - Return a single book by ID (return 404 if not found)
- `POST /books` - Create a new book and return it with status code 201
- `PUT /books/{book_id}` - Update an existing book (return 404 if not found)
- `DELETE /books/{book_id}` - Delete a book and return status code 204 (return 404 if not found)
- Use appropriate HTTP status codes and response models
- Handle errors gracefully with HTTPException

Example responses:

```json
// GET /books
[
  {
    "id": 1,
    "title": "The Python Handbook",
    "author": "Jane Smith",
    "year": 2023,
    "isbn": "978-0-123456-78-9"
  }
]

// POST /books
{
  "id": 4,
  "title": "FastAPI in Action",
  "author": "John Doe",
  "year": 2024,
  "isbn": "978-0-987654-32-1"
}
```
