def format_phone_number(phone):
    a = phone.replace("()", "").replace("-", "").replace(" ", "")
    if len(a) == 10:
        return f"({a[0:3]}) - {a[3:6]} - {a[6:10]}"
    return "Invalid phone number"


print(format_phone_number("555-123-4567"))  # (555) - 123 - 4567
print(format_phone_number("(555) 123 4567"))  # (555) - 123 - 4567
print(format_phone_number("5551234567"))  # (555) - 123 - 4567
print(format_phone_number("123"))  # Invalid phone number
print()


# def sanitize_filename(filename):
#     clean = filename.lower().replace(" ", "_")
#     allowed = ""
#     for char in clean:
#         if char.isalnum() or char in ".-_":
#             allowed += char

#     if allowed.endswith(".txt"):
#         result = allowed
#     else:
#         if "." in allowed:
#             dot_pos = allowed.rfind(".")
#             allowed = allowed[:dot_pos]
#         result = allowed + ".txt"


#     if len(result) > 50:
#         max_base = 50 - 4
#         result = result[:max_base] + ".txt"
#     return result
def sanitize_filename(filename):
    clean = filename.lower().replace(" ", "_")
    safe = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            safe += char

    if not safe.endswith(".txt"):
        if "." in safe:
            safe = safe[: safe.rfind(".")]
        safe += ".txt"

    if len(safe) > 50:
        safe = safe[:46] + ".txt"

    return safe


print(sanitize_filename("Ancient Scroll.txt"))  # "ancient_scroll.txt"
print(sanitize_filename("Quest 2042! (Epic)"))  # "quest_2042_epic.txt"
print(sanitize_filename("notes"))  # "notes.txt"
print(sanitize_filename("X" * 100))
# "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.txt"
