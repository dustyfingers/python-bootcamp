# sets are like formal mathematical sets
# no order, no dupes
s = {1, 4, 5}

# or
s2 = set({1, 4, 5})

for element in s:
    print(element)

# set methods in python
s.add(6)
for element in s:
    print(element)

s.remove(4)

s.discard(5)

another_set = s.copy()


# set math methods
# union
print(s2 | s)
# intersection
print(s & s2)
