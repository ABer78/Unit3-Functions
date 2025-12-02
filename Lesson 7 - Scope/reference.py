# Scope - the visibility of variables; where it can be seen and used
# Global - outside all functions (visible everywhere)
# Local - inside a function (only visible in a function)


# The BUG - Crashes (UnboundLocalError)
def add_bonus():
    score = score + 100  # Python thinks it is local
    print(f"Your score: {score}")


score = 100
add_bonus
