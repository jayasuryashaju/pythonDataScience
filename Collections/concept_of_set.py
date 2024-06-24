"""
set:
    how to define ?
        st = {1, 2, 3}
        set must be defined using set function, or
        you must pass values when creating a set using curly braces.
properties:
    supports heterogeneous data.
    insertion order not preserved.
    set not support duplicate values.
    set is mutable

"""

st = set()
st1 = {1, 2, 4}
print(type(st))
st.add(23)
print(st)

st2 = {1, 2, "python", "luminar", True, False, 10.5}
print(st2)

st3 = {10, 20, 30, 20, 30, 40, 50, 60, 40, 20}
print(st3)

st4 = {1, 0, True, False}
print(st4)

st2.remove("luminar")
print(st2)