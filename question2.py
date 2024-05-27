# Question 2 Task 1

def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Added '{title}' by {author} to the library.")
    else:
        print(f"'{title}' by {author} already exists in the library.")

# Example usage:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library, "1984", "George Orwell")  # Duplicate book
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")  # New book
add_book(library, "Brave New World", "Aldous Huxley")  # Duplicate book
