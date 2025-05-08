LARGE_BOOK_LIST = [
    # Fiction
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction", "language": "English", "price": 12.99, "cover_url": "https://m.media-amazon.com/images/I/71FxgtFKcQL._AC_UF1000,1000_QL80_.jpg", "description": "A classic novel about racial injustice and moral growth in the American South during the 1930s.", "isbn": "9780446310789", "pages": 281, "publisher": "Grand Central Publishing", "publication_date": "1988-10-11"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction", "language": "English", "price": 9.99, "cover_url": "https://m.media-amazon.com/images/I/71FTb9X6wsL._AC_UF1000,1000_QL80_.jpg", "description": "A story of decadence and excess, exploring themes of the American Dream and social class in the 1920s.", "isbn": "9780743273565", "pages": 180, "publisher": "Scribner", "publication_date": "2004-09-30"},
    {"title": "1984", "author": "George Orwell", "category": "Fiction", "language": "English", "price": 10.99, "cover_url": "https://m.media-amazon.com/images/I/71kxa1-0mfL._AC_UF1000,1000_QL80_.jpg", "description": "A dystopian novel set in a totalitarian society ruled by Big Brother.", "isbn": "9780451524935", "pages": 328, "publisher": "Signet Classic", "publication_date": "1950-07-01"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Fiction", "language": "English", "price": 8.99, "cover_url": "https://m.media-amazon.com/images/I/81OthjkJBuL._AC_UF1000,1000_QL80_.jpg", "description": "A romantic novel that charts the emotional development of the protagonist Elizabeth Bennet.", "isbn": "9780141439518", "pages": 279, "publisher": "Penguin Classics", "publication_date": "2002-12-31"},
    {"title": "Godan", "author": "Munshi Premchand", "category": "Fiction", "language": "Hindi", "price": 8.99, "cover_url": "https://m.media-amazon.com/images/I/81QKQ9mwV7L._AC_UF1000,1000_QL80_.jpg", "description": "A classic Hindi novel depicting the life of Indian peasants and their struggles with poverty and social injustice.", "isbn": "9788122200714", "pages": 320, "publisher": "Raja Pocket Books", "publication_date": "1936-01-01"},
    # ... 20 more Fiction books with valid cover_url ...
    # Non-Fiction
    {"title": "Educated", "author": "Tara Westover", "category": "Non-Fiction", "language": "English", "price": 13.99, "cover_url": "https://m.media-amazon.com/images/I/81WojUxbbFL._AC_UF1000,1000_QL80_.jpg", "description": "A memoir about a woman who grows up in a survivalist family and eventually escapes to learn about the world through education.", "isbn": "9780399590504", "pages": 352, "publisher": "Random House", "publication_date": "2018-02-20"},
    # ... 24 more Non-Fiction books ...
    # Science
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Science", "language": "English", "price": 14.99, "cover_url": "https://m.media-amazon.com/images/I/A1xkFZX5k-L._AC_UF1000,1000_QL80_.jpg", "description": "A landmark volume in science writing exploring the mysteries of space, time, and black holes.", "isbn": "9780553380163", "pages": 212, "publisher": "Bantam", "publication_date": "1998-09-01"},
    # ... 24 more Science books ...
    # Technology
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Technology", "language": "English", "price": 19.99, "cover_url": "https://m.media-amazon.com/images/I/41xShlnTZTL._AC_UF1000,1000_QL80_.jpg", "description": "A handbook of agile software craftsmanship that teaches how to write clean, maintainable code.", "isbn": "9780132350884", "pages": 464, "publisher": "Prentice Hall", "publication_date": "2008-08-11"},
    # ... 24 more Technology books ...
    # Repeat for all other categories, ensuring at least 25 books per category, with a mix of languages and authors, and all with valid cover_url.
] 

from books_data import LARGE_BOOK_LIST
print(len(LARGE_BOOK_LIST))

POPULAR_BOOKS = LARGE_BOOK_LIST 