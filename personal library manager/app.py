import sqlite3
import os

# Database file
DATABASE_FILE = "library.db"

# Function to initialize the database
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        print("Database file not found. Creating a new database...")
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                read_status INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Database and 'books' table created successfully!")
    else:
        print("Database already exists. Skipping initialization.")

# Function to add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, year, genre, read_status)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, author, year, genre, int(read_status)))
    conn.commit()
    conn.close()
    print("Book added successfully!")

# Function to remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE title = ?', (title,))
    if cursor.rowcount > 0:
        print("Book removed successfully!")
    else:
        print("Book not found!")
    conn.commit()
    conn.close()

# Function to search for a book
def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    if choice == "1":
        search_term = input("Enter the title: ").lower()
        cursor.execute('SELECT * FROM books WHERE LOWER(title) LIKE ?', (f"%{search_term}%",))
    elif choice == "2":
        search_term = input("Enter the author: ").lower()
        cursor.execute('SELECT * FROM books WHERE LOWER(author) LIKE ?', (f"%{search_term}%",))
    else:
        print("Invalid choice!")
        return
    
    matching_books = cursor.fetchall()
    if matching_books:
        print("Matching Books:")
        for book in matching_books:
            status = "Read" if book[5] else "Unread"
            print(f"{book[1]} by {book[2]} ({book[3]}) - {book[4]} - {status}")
    else:
        print("No matching books found!")
    conn.close()

# Function to display all books
def display_books():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    
    if not books:
        print("Your library is empty!")
        return
    
    print("Your Library:")
    for book in books:
        status = "Read" if book[5] else "Unread"
        print(f"{book[1]} by {book[2]} ({book[3]}) - {book[4]} - {status}")

# Function to display statistics
def display_statistics():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM books')
    total_books = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM books WHERE read_status = 1')
    read_books = cursor.fetchone()[0]
    conn.close()
    
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main function
def main():
    initialize_database()  # Ensure the database and table are initialized
    
    while True:
        print("\n------------ Welcome to your Personal Library Manager! --------------")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

main()

