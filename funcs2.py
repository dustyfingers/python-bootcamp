# *args and **kwargs
# def sum_all_nums(num1, num2, num3):
#     return num1 + num2 + num3


# print(sum_all_nums(1, 2, 3))


# what about any number of args?
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums(1, 2, 3))
