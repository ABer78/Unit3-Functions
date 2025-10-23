"""
Feature: JavaScript; Python
Create: [1, 2, 3]; [1, 2, 3]
Add: .push(val); .append(val)
Remove end: .pop(); .pop()
Insert: .insert(index, val)

"""

# Creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]

# Accessing elements
first_day = daily_likes[0]
last_day = daily_likes[-1]
third_day = daily_likes[2]

# Slicing
first_three = daily_likes[0:3]
last_two = daily_likes[-2:]


"""
length: length = len()
max: maximum = max()
min: minumum = min()
"""


# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty"


def format_usernames(handles):
    formatted = []
    for name in handles:
        formatted.append("@" + name)
    return formatted


# Test:
result = format_usernames(["nasa", "tswift", "netflix"])
print(result)  # ['@nasa', '@tswift', '@netflix']

print()


def filter_trending_posts(likes_list):
    trending = []
    for likes in likes_list:
        if likes > 1000:
            trending.append(likes)
    return trending


result1 = filter_trending_posts([500, 1200, 800, 1500, 600])
print(result1)  # [1200, 1500]
