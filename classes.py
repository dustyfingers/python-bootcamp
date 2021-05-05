class User:
    # the __init__ method is run upon object instantiation
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    pass


user1 = User("Joe", "White", 42)
user2 = User("Blanca", "Green", 22)
