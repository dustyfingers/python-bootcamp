numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
sum = 0

for number in numbers:
    sum += (1 / (number ** 2))
print(sum)


while i < len(numbers):
    print(numbers[i])
    i += 1
