with open("data.txt") as file:
    data = file.read()

data = data.split("\n")
tickets = {x: 1 for x in range(len(data))}
for l, line in enumerate(data):
    winning = line.split(": ")[1].split(" | ")[0].split(" ")
    ours = line.split(": ")[1].split(" | ")[1].split(" ")
    ours = [i for i in ours if i != " " and i != ""]

    union = list(set(ours) & set(winning))

    for i in range(1, len(union) + 1):
        if l + i in tickets:
            tickets[l + i] = tickets[l + i] + tickets[l]

sum = sum(tickets.values())

print(sum)
