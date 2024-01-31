# Flask Book API

Flask-Book-API is a straightforward Flask application designed for managing a collection of books through a RESTful API. This project supports basic CRUD (Create, Read, Update, Delete) operations, enabling users to interact with book records stored in a MySQL database. The API also includes basic authentication using Flask-BasicAuth for added security.

# Features

    Create Book: Add new books to the database with specified titles and authors.
    Get Books: Retrieve a list of all books in the database.
    Get Book by ID: Fetch details of a specific book using its unique identifier.
    Update Book: Modify the title or author information of an existing book.
    Delete Book: Remove a book from the database.

# Technologies Used

    Flask: A micro web framework for Python.
    Flask-MySQLdb: Flask extension for MySQL integration.
    Flask-BasicAuth: Flask extension for basic HTTP authentication.

# Setup Instructions

    Clone the repository.
    Set up a virtual environment and install dependencies.
    Configure MySQL database details in the app.py file.
    Activate the virtual environment.
    Run the Flask application with python app.py.
    Utilize tools like Postman to interact with the API endpoints.

# API Endpoints

    POST /api/books: Create a new book.
    GET /api/books: Retrieve all books.
    GET /api/books/{book_id}: Retrieve details of a specific book.
    PUT /api/books/{book_id}: Update an existing book.
    DELETE /api/books/{book_id}: Delete a book.

# Sample Request (Postman)
## POST /api/books

    URL: http://127.0.0.1:5000/api/books
    Method: POST
    Headers:
        Content-Type: application/json
        Authorization: Basic base64(username:password)
    Body:

json

{
"title": "Sample Book",
  "author": "John Doe"
}
