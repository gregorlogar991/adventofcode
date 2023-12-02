with open("data.txt") as file:
    data = file.read()

solution = 0
for line in data.strip().split():
    letter_nums = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    first_digit = None
    last_digit = None

    for i in range(len(line)):
        current = None
        c = line[i]

        if c.isdigit():
            current = int(c)

        for j, letter_num in enumerate(letter_nums):
            if line[i : (i + len(letter_num))] == letter_num:
                current = j + 1
                break

        if current:
            if first_digit == None:
                first_digit = current
            last_digit = current

    solution += first_digit * 10 + last_digit
    print(first_digit, " ", last_digit, " ", solution)


print("Solution:", solution)
