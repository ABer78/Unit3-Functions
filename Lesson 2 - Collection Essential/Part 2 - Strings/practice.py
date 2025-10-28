# Question 3
def create_username(first_name, last_name):
    combine = first_name + "_" + last_name
    return combine.lower()
    # return f"{first_name}_{last_name}".lower()


print(create_username("Hi", "there"))
print()


# Question 5
def check_email(email):
    if "@" in email and email.lower().endswith(".com"):
        return True
    return False
    # email_lower = email.lower()
    # return "@" in email_lower and email_lower.endswith(".com")


print(check_email("bergen_tech@gmail.com"))  # True
print(check_email("bergen_tech@gmail.org"))  # False
print(check_email("bergen_tech.gmail.com"))  # False
print()


# Question 9
def create_slug(title):
    lower = title.lower()
    remove = lower.strip()
    replace = remove.replace(" ", "-")
    return replace
    # return title.lower().strip().replace(" ", "-")


print(create_slug(" Hi There "))
print()
