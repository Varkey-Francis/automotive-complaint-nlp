with open("data/FLAT_CMPL.txt", "r", encoding="latin-1") as f:
    for i, line in enumerate(f):
        print(repr(line[:300]))
        if i >= 3:
            break