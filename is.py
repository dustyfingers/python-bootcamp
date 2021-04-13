a = 1
a == 1  # True
a is 1  # True


c = [1, 2, 3]
d = [1, 2, 3]
c == d  # True
c is d  # False

e = d
d is e  # True
