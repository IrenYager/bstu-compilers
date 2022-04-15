TABLE_SIZE = 5
MASS = [[] for i in range(TABLE_SIZE)]


def hash(ident):
    if len(ident) < 3:
        ident += chr(0)*(3-len(ident))
    ident = ident.upper()
    number = ord(ident[0])+ord(ident[1])+ord(ident[2])
    return number


def insert(ident):
    id = hash(ident) % TABLE_SIZE
    for i in range(len(MASS[id])):
        if MASS[id][i] > ident:
            MASS[id].insert(i, ident)
            return
    MASS[id].append(ident)


def find(ident):
    id = hash(ident) % TABLE_SIZE
    if ident in MASS[id]:
        return True
    else:
        return False


with open('text.txt', 'r') as fp:
    for word in fp:
        insert(word.strip())

for item in MASS:
    print(item)

if find(input()):
    print("word was found")