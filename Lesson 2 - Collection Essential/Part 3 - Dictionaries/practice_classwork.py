# Question 1:
# {"key_a": "value1", "key_b": 150, "key_d": 50}
# False


# Question 2:
# 120
# 60


# Question 3:
def get_user_bio(user):
    bio = user.get("bio")
    if bio == None:
        return "No bio available"
    return bio
 

print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))
# "Python enthusiast"
print(get_user_bio({"username": "newbie"}))  # "No bio available"
print()


# Question 4:
# 60
# 160


# Question 5:
# 2


# Question 6:
def get_total_engagement(post):
    likes = post.get("likes", 0)
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    total = likes + comments + shares
    return total


print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))  # 130
print(get_total_engagement({"likes": 50, "comments": 5}))  # 55
print(get_total_engagement({"views": 1000}))  # 0
print()


# Question 7:
# 3
# 3


# Question 8:
# {'key1': 'value1', 'key2': 200, 'key3': 50}
# {'key1': 'value1', 'key2': 100, 'key4': True}


# Question 9:
def find_most_followed(users):
    most = 0
    most_followed = {}
    for user in users:
        if user.get("followers") > most:
            most = user.get("followers")
            most_followed = user
    return most_followed


users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000},
]
print(find_most_followed(users))
