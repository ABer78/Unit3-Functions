# Question 1
# 2300

# Question 2
# WOW WOW LFG

# Question 3
def find_top_donor(donations):
    top_donor = ""
    top_amount = -1
    for name, amount in donations.items():
        if amount > top_amount:
            top_amount = amount
            top_donor = name
    return top_donor
            

donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations)) # lunar
