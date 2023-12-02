with open("data.txt") as file:
    data = file.read()

sum = 0
for line in data.split("\n"):
    max = {"green": 0, "red": 0, "blue": 0}
    print("line: ", line.split(":")[1].split(";"))
    for games in line.split(":")[1].split(";"):
        print("game: ", games)
        for game in games.split(","):
            print(game)
            if int(game.lstrip().split(" ")[0]) > max[game.lstrip().split(" ")[1]]:
                max[game.lstrip().split(" ")[1]] = int(game.lstrip().split(" ")[0])
    print(max)
    sum += max["green"] * max["red"] * max["blue"]

print(sum)
