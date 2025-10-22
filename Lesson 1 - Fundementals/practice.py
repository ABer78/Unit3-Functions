# Question 3:
def calculate_discount(price, member_status):
    if member_status == "premium":
        return price * 0.7  # 30% off
    elif member_status == "standard":
        return price * 0.85  # 15% off
    return price


print(calculate_discount(100, "premium"))  # 70.0
print(calculate_discount(100, "standard"))  # 85.0
print(calculate_discount(100, "guest"))  # 100

print()


# Question 6:
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))  # 1
print(count_vowels("AEIOU"))  # 5


# Question 9:
def validate_password(password):
    if len(password) < 8:
        return False

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
    return has_digit
