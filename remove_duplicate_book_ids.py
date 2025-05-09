import json
from collections import Counter
import random
import string

# Load books
with open('srp/books.json', encoding='utf-8') as f:
    books = json.load(f)

# Find duplicate IDs
id_counts = Counter(book['id'] for book in books if 'id' in book)
duplicates = {bid for bid, count in id_counts.items() if count > 1}

seen = set()
unique_books = []
for book in books:
    bid = book.get('id')
    if bid in seen:
        # If duplicate, assign a new random unique ID
        new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        while new_id in id_counts or new_id in seen:
            new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        book['id'] = new_id
        seen.add(new_id)
    else:
        seen.add(bid)
    unique_books.append(book)

# Save the cleaned list
with open('srp/books.json', 'w', encoding='utf-8') as f:
    json.dump(unique_books, f, indent=2, ensure_ascii=False)

print(f"Fixed duplicate IDs. {len(duplicates)} duplicates found and replaced.")
