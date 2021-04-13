numbers = (1, 2, 3, 4, 2)

# different from a list in that it is immutable!


# methods
3 in numbers  # True

# tuples are also faster than lists!
# it can make your code safer from bugs
# a tuple is a valid key in a dictionary!


# so imagine if you know some ordered data is never going to change?
# months of the year, days of the week, etc


# access works just like a list
numbers[2]  # 3


locations = {
    (131.2243, 39.7764): "Tokyo Office",
    (40.7124, 16.2352): "New York Office"
}

# some dictionary methods return tuples (.items())
cat = {"name": "biscuit", "age": 4, "fav_toy": "fuzzy ball"}

print(cat.items())


numbers.count(1)  # returns 1
numbers.count(2)  # returns 2
numbers.index(1)  # returns 0
