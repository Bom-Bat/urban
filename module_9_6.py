def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            n = j + i
            if n <= len(text):
                yield text[j:n]


a = all_variants("abc")

for i in a:
    print(i)