# not associated in any way
item1 = 'bana'
item2 = 'lego'

# associated, but weird and hard to manipulate
silly_string = 'paper///microwave///towel'

# list!
my_list = [item1, item2, 'item three here']

# list comprehensions
# [print(item.upper()) for item in my_list]
# print(my_list)  # the original list remains unmutated

# print([item[2].upper() for item in my_list])
# print(my_list)

capitalized_list_short = [item for item in my_list if len(item) <= 4]
capitalized_list_long = [item for item in my_list if len(item) > 4]

print(capitalized_list_long)
print(capitalized_list_short)
