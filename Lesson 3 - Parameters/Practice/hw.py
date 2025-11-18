# Question 5
# 18.0
# 15.0


# Question 6
def make_notification(user, *messages, urgent=False):
    message_string = ", ".join(messages)
    prefix = "URGENT: " if urgent else ""
    return f"{prefix}{user} - {message_string}"


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
    actions_string = ", ".join(actions)
    context_pairs = []
    for key, value in context.items():
        context_pairs.append(f"{key}={value}")
    context_string = ", ".join(context_pairs)
    log = f"{actor}: {actions_string}"
    if context_string:
        log += f" | {context_string}"
    return log


print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))
# bot: login, scan | source=API, ip = 1.2.3.4
