games = ["CSGO", "PUBG", "Leage of Legend","Star Craft 2"]
print(*games,sep=", ")

prefixes = ["I","II","III","IV","V"]


new_games = input("Which game would you like to update?")

pos = int(input("Which positon would you like to replace?")) - 1

games[pos] = new_games

i = 0

for game in games:
    p = prefixes[i]
    text = "{0}. {1}".format(p, game)
    i += 1

    print(text)
