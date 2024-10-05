#Task 1: Library System Enhancement
def add_book(library, new_book):
    # Check if the book already exists in the library
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        # Add the new book to the library
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Example usage
new_book_1 = ("To Kill a Mockingbird", "Harper Lee")
new_book_2 = ("1984", "George Orwell")  # Duplicate book

add_book(library, new_book_1)  # Adding a new book
add_book(library, new_book_2)  # Attempting to add a duplicate book

# Print the updated library
print("\nUpdated Library:")
for book in library:
    print(f"{book[0]} by {book[1]}")
