import json
from books_data import LARGE_BOOK_LIST

# This script exports LARGE_BOOK_LIST to books.json in the project root
import random
import string

def assign_book_ids_and_quantities(book_list):
    for book in book_list:
        if 'id' not in book or not book['id']:
            # Generate a random 6-character alphanumeric ID
            book['id'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if 'quantity' not in book or not isinstance(book['quantity'], int):
            book['quantity'] = 10
        if 'available' not in book or not isinstance(book['available'], int):
            book['available'] = book['quantity']
    return book_list

def export_books_to_json():
    books_with_all_fields = assign_book_ids_and_quantities(LARGE_BOOK_LIST)
    # Export to books.json in root
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books_with_all_fields, f, ensure_ascii=False, indent=2)
    # Export to srp/books.json
    with open('srp/books.json', 'w', encoding='utf-8') as f:
        json.dump(books_with_all_fields, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    export_books_to_json()
