# Advanced API Project

## Overview
This project demonstrates the use of Django REST Framework's generic views to implement CRUD operations for the Book model.

## Endpoints
- `GET /api/books/` - List all books (public).
- `GET /api/books/<id>/` - Retrieve a single book by ID (public).
- `POST /api/books/create/` - Create a new book (authenticated users).
- `PUT /api/books/<id>/update/` - Update an existing book (authenticated users).
- `DELETE /api/books/<id>/delete/` - Delete a book (authenticated users).

## Permissions
- List and Detail views are accessible to all users.
- Create, Update, and Delete views are restricted to authenticated users.

## Testing
Use tools like Postman or curl to test the API.
