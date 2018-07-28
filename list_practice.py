games = ["CSGO", "PUBG", "Leage of Legend", "Star Craft 2"]
print(*games,sep=", ")

new_games = input("What games would you like to add?")

games.append(new_games)
print(*games,sep=", ")

remove_game = input("What game would you like to remove?")
games.remove(remove_game)
print(*games,sep=", ")

for game, index in enumerate(games):
    print(game, "." , index)

pos_remove = int(input("Postion to remove = ? "))

games.pop(pos_remove)


for game, index in enumerate(games):
    print(game, "." , index)
