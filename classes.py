class User:
    # class attributes
    # instance attributes are unique for each instance of a class (first, last, age)
    # class attributes are explicitly defined on the class and are the same on each instance
    active_users = 100

    # the __init__ method is run upon object instantiation
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    # this is a method
    def full_name(self):
        print(f"{self.first} {self.last}")


user1 = User("Joe", "White", 42)
user2 = User("Blanca", "Green", 22)
user2.full_name()
# accessed by calling the class its self
print(User.active_users)
