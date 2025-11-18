# Question 5
# 18.0
# 15.0


# Question 6
def make_notification(user, *messages, urgent=False):
    if urgent == True:
        urgent = "URGENT"
        return urgent, user, *messages
    return user, *messages


print(make_notification("admin", "Server down!", urgent=True))
# "URGENT: admin - Server down!"
print(make_notification("user", "Welcome", "Check inbox"))
# "user - Welcome, Check inbox"
print()


# Question 7
# SELECT name,email FROM users LIMIT 10
# SELECT * FROM logs WHERE level='error' LIMIT 5


# Question 8
def log_action(actor, *actions, timestamp=None, **context):
    return f"{actor}: {actions} | {context}"


print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))
# bot: login, scan | source=API, ip = 1.2.3.4
