import re

with open("data.txt") as file:
    data = file.read()

solution = 0
for line in data.strip().split():
    numbers = re.findall("\\d", line)
    solution += int(numbers[0] + numbers[-1])

print("Solution: ", solution)
