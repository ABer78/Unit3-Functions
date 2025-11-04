# Question 2:
def find_top_players(players, min_score):
    top_players = []
    for player in players:
        if player["score"] >= min_score:
            top_players.append(player["username"])
    return top_players


players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800},
]

result = find_top_players(players, 7000)
print(result)  # ['DragonSlayer', 'MageKing']
print()

# Question 3:

# Total songs: 9
# First songs: EYE OF THE TIGER
# Last song: BLINDING LIGHTS


# Question 4:
def calculate_cart_total(cart):
    total = 0
    for item in cart:
        item_cost = item["price"] * item["quantity"]
        total += item_cost
    return total


cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3},
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")  # Total: $1059.93
