# convention for 'private' properties
# name
# will mangle the name of this prop
# __name
# dunder method
# __name__

# dunder methods are special methods python looks for chen instnatiating an object from a class
class Person:
    def __init__(self):
        self.name = "tony"
        # private vars and methods dont actually exist in python this is just convention
        self._secret = "hi!"
        # try to access this __message prop i dare u
        self.__message = "I like turtles"


p = Person()
print(p.name)
print(p._secret)

# python will 'mangle' this property name behind the scenes, isnt that cool?
# print(p.__message)
# still accessible though
print(p._Person__message)


# ...but why tho?
# makes this prop particlar to THIS class...eg a classs that inherits from person can also
# have its own 'message' property
