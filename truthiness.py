# things that eval to False in python
if '':
    print("this wont print!")
if 0:
    print("this wont print!")
if {}:
    print("this wont print!")
if None:
    print("this wont print!")

# things that eval to True in python
if 'string here':
    print("this will print!")
if 1:
    print("this will print!")

animal = input("What is your favorit animal?")

if animal:
    if animal == "goose":
        print("You are sick!!")
    else:
        print("You said " + animal + " was your favorite animal.")
else:
    print("You didnt say anything!!!")
