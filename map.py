nums = [1,2,3,4]
doubles = list(map(lambda num: num * 2, nums))

# iterable map object
for num in doubles:
    print(num)


# cast as a list to print
print(doubles)