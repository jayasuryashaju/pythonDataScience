"""
to add a value to a set use add() function.

st = {1, 2, 3}
st.add(4)
add() function can only add one value at a time.
to add multiple values  update() function is used.

remove() function is used to remove values from a set
st.remove(10)

pop() function can also be used to remove some random element

discard() function can also be used to remove an element from a set.
    Unlike set.remove(), the discard() method does not raise
    an exception when an element is missing from the set.



"""

st = {10, 15, 40, 30}

st.add(70)

st.update([1, 35, 85])

st.remove(10)
st.pop()
st.discard(33)

print(st)

