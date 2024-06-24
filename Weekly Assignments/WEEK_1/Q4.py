def generate_identifiers(n):
    if n < 1:
        return []
    first_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    subsequent_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

    identifiers = []
    current_identifiers = list(first_chars)

    for length in range(1, n):
        next_identifiers = []
        for identifier in current_identifiers:
            for char in subsequent_chars:
                next_identifiers.append(identifier + char)
        current_identifiers = next_identifiers

    return current_identifiers


n = int(input("Enter the length of the identifier: "))

identifiers = generate_identifiers(n)
for identifier in identifiers:
    print(identifier)

print("Total number of identifiers:", len(identifiers))
