with open("data.txt") as file:
    data = file.read()

sum = 0
for line in data.split("\n"):
    max = {"green": 0, "red": 0, "blue": 0}
    for games in line.split(":")[1].split(";"):
        for game in games.split(","):
            print(game)
            if int(game.lstrip().split(" ")[0]) > max[game.lstrip().split(" ")[1]]:
                max[game.lstrip().split(" ")[1]] = int(game.lstrip().split(" ")[0])
    sum += max["green"] * max["red"] * max["blue"]

print(sum)
