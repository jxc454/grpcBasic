def scratchFunc():
    s = [a**2 for a in range(100) if not a % 10]    
    # printArray(s)

    dict = {"a": 1, "b": 2, "c": 3, "d": 3, "e": 4}
    # print(dict)
    # print({number: letter for letter, number in dict.items()})
    # print({number for letter, number in dict.items()})

    # d = [a for a in range(100) if not a in [6, 7, 8] if a % 10]
    # printArray(d)

    d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    d = [x for row in reversed(d) for x in reversed(row)]
    printArray(d)


def printArray(arr):
    print(', '.join([str(x) for x in arr]))

def consume(val):
    yield val + 1

if __name__ == '__main__':
    consumer = consume(None)
    i = 0
    while i < 10:
        i += consume(i)