# Question 1
# [23]

# Question 2
# NEXUS


# Question 3
def match_mvp(players):
    best_ratio = 0
    mvp = ""
    for name, stats in players.items():
        ratio = stats["kills"]/stats["deaths"]
        if ratio > best_ratio:
            best_ratio = ratio
            mvp = name
    return mvp


players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18},
}

print(match_mvp(players))
