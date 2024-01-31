from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_basicauth import BasicAuth

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'MYSQLusername'
app.config['MYSQL_PASSWORD'] = 'MYSQLpassword'
app.config['MYSQL_DB'] = 'MYSQLdatabasename'

mysql = MySQL(app)

# BasicAuth configurations
app.config['BASIC_AUTH_USERNAME'] = 'username' # Placeholder for connecting to POSTMAN
app.config['BASIC_AUTH_PASSWORD'] = 'password' # Placeholder for connecting to POSTMAN
basic_auth = BasicAuth(app)

# Route to create a new book
@app.route('/api/books', methods=['POST'])
@basic_auth.required
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Book created successfully"}), 201

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    
    book_list = []
    for book in books:
        book_dict = {
            "id": book[0],
            "title": book[1],
            "author": book[2]
        }
        book_list.append(book_dict)
    
    return jsonify(book_list)

# Route to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cur.fetchone()
    cur.close()
    
    if book:
        book_dict = {
            "id": book[0],
            "title": book[1],
            "author": book[2]
        }
        return jsonify(book_dict)
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to update a book by ID
@app.route('/api/books/<int:book_id>', methods=['PUT'])
@basic_auth.required
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE books SET title = %s, author = %s WHERE id = %s", (title, author, book_id))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Book updated successfully"})

# Route to delete a book by ID
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
@basic_auth.required
def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
