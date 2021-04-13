def first_function():
    print('this is my first function (not really tho)!!!')


first_function()


def full_name(first, last):
    return f"Your full fame is {first} {last}"


# setting a default parameter
def full_name_w_kwargs(first="Louie", last="Williford"):
    """this is a docstring. it should simply summarize the function."""
    return f"Your full fame is {first} {last}"


print(full_name_w_kwargs())
# with passed keyword arguments
print(full_name_w_kwargs(first="Ed"))

print(full_name_w_kwargs.__doc__)
