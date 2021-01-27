games = []

games.extend(["red dead redemption", "gta v", "gta iv"])
games.append("LA Noire")
games.remove("gta iv")

if "red dead" or "red dead redemption" in games:
    games.insert(0, "rockstar games: ")
    print(games)