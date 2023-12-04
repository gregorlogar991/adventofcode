with open("data.txt") as file:
    data = file.read()
sum = 0
for line in data.split("\n"):
    cards = line.split(": ")[1]
    winning = cards.split(" | ")[0].split(" ")
    ours = cards.split(" | ")[1].split(" ")
    ours = [i for i in ours if i != " " and i != ""]

    union = list(set(ours) & set(winning))

    if union != []:
        sum += pow(2, len(union) - 1)

print(sum)
