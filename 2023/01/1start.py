import re

with open("data.txt") as file:
    data = file.read()

solution = 0
for line in data.strip().split():
    numbers = re.findall("\d", line)
    print(numbers, " ", int(numbers[0]) * 10 + int(numbers[-1]))
    solution += int(numbers[0]) * 10 + int(numbers[-1])

print("Solution: ", solution)
