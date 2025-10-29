# Question 1:
# Output: "john.smith gmail.com"


# Question 2:
# Output: "tqbf"


# Question 3:
def extract_domain(email):
    if email.count("@") == 1:
        return email.split("@")[1].lower()
    return "Invalid email"


print(extract_domain("john@gmail.com"))  # "gmail.com"
print(extract_domain("JANE@YAHOO.com"))  # "yahoo.com"
print(extract_domain("missing.at.sign.com"))  # "Invalid email"
print(extract_domain("too@@many@signs.com"))  # "Invalid email"
print()

# Question 4:
# Output: "123456"


# Question 5:
# Output: MY_DOCUMENT


# Question 6:
# Output: "banana"


# Question 7:
def filter_numbers(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result


print(filter_numbers("Hello123World456"))  # "HelloWorld"
print(filter_numbers("Test 1 2 3"))  # "Test   "
print(filter_numbers("Price: $29.99"))  # "Price: $"
print(filter_numbers("No numbers here!"))  # "No numbers here!"
print()

# Question 8:
# Output: "https://examples.com/users/profile"


# Question 9:
def count_character_types(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if "A" <= char <= "z":
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1
    return f"letters: {letters}, digits: {digits}, spaces: {spaces}"


print(count_character_types("Hello 123"))  # "letters: 5, digits: 3, spaces: 1"
print(count_character_types("Test2024!"))  # "letters: 4, digits: 4, spaces: 0"
