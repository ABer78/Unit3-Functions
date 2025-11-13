# Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile"""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online,
    }


player1 = create_gamer(
    username="BTStudent", level=25, xp=10000, rank="gold", online=True
)

print(player1)
# {'username': 'BTStudent', 'level': 25, 'xp': 10000, 'rank': 'gold', 'online': True}
print()


def send_message(sender, recipient, message, urgent):
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"


messenger = send_message(
    sender="Alex", recipient="Jordan", message="Check discord", urgent=True
)

print(messenger)  # Alex -> Jordan: Check discord (Urgent: True)
print()


def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️  {likes}  🔄️ {retweets}"


UserPost = post_content(username="techguru", text="Python is amazing!")

print(UserPost)


# *args - Accept any number of values
def sum_scores(*scores):
    """ Sum any number of scores """
    total = 0
    for score in scores:
        total += score
    return total

result1 = sum_scores(10, 20, 30)
result2 = [10, 20, 30]

print(result1)# 60
print(result2)# 60
