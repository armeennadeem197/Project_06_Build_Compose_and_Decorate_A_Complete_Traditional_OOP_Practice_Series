# This script allows users to add books and keeps track of the total number of books added.
class Book:
    total_books = 0

    def __init__(self, name):
        self.name = name
        print(f"📚 Book '{self.name}' created.")

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"🔢 Total books: {cls.total_books}")

    @classmethod
    def add_book(cls, name):
        book = cls(name)
        cls.increment_book_count()
        return book

# Start the loop
print("📖 Welcome to the Book Manager!")
print("Type 'exit' to stop adding books.\n")

while True:
    book_name = input("Enter book name: ")
    if book_name.lower() == "exit":
        print("\n Final book count:", Book.total_books)
        print("\n🚪 Exiting...")
        break
    Book.add_book(book_name)