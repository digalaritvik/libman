import csv

final_books = []

with open('books.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Adjust indices if your CSV columns differ
        # Example: [ASIN, filename, image_url, title, author, category_id, category]
        book = {
            "title": row[3],
            "author": row[4],
            "category": row[6],
            "language": "English",
            "price": 9.99,
            "cover_url": row[2],
            "description": "",
            "isbn": row[0],
            "pages": 200,
            "publisher": "",
            "publication_date": ""
        }
        final_books.append(book)

# Save to a Python file
with open('books_data.py', 'w', encoding='utf-8') as f:
    f.write('LARGE_BOOK_LIST = [\n')
    for book in final_books:
        f.write(f'    {book},\n')
    f.write(']\n')

from books_data import LARGE_BOOK_LIST
print(len(LARGE_BOOK_LIST))