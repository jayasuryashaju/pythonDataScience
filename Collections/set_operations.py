"""
set operations:
    1. union
    2. intersection
    3. difference

1. union
    combined result of two sets

2. intersection
    common elements in two sets

3. difference
    st1.difference(st2)
        elements that are only present in st1
    st2.difference(st1)
        elements that are only present in st2

"""
st1 = {1, 2, 3, 4, 5}
st2 = {3, 4, 5, 6, 7, 8}

print(st1.union(st2))

print(st1.difference(st2))
print(st2.difference(st1))

print(st1.intersection(st2))
