with open("data.txt") as file:
    data = file.read()
bag_contain = {"red": 12, "green": 13, "blue": 14}
sum = 0

for line in data.split("\n"):
    possible = True
    for games in line.split(":")[1].split(";"):
        for game in games.split(","):
            if (
                int(game.lstrip().split(" ")[0])
                > bag_contain[game.lstrip().split(" ")[1]]
            ):
                possible = False
    if possible:
        sum += int(line.split(":")[0].replace("Game ", ""))

print(sum)
