import json

# Path to your books.json file
f = 'srp/books.json'

with open(f, encoding='utf-8') as file:
    arr = json.load(file)

seen = set()
out = []
for b in arr:
    if b['id'] not in seen:
        out.append(b)
        seen.add(b['id'])

with open(f, 'w', encoding='utf-8') as file:
    file.write('[\n')
    for i, b in enumerate(out):
        block = json.dumps(b, ensure_ascii=False, indent=2)
        block = '  ' + block.replace('\n', '\n  ')
        file.write(block)
        if i != len(out) - 1:
            file.write(',\n')
        else:
            file.write('\n')
    file.write(']')
