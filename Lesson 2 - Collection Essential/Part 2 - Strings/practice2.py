def format_phone_number(phone):
    a = phone.replace("()", "").replace("-", "").replace(" ", "")
    if len(a) == 10:
        return f"({a[0:3]}) - {a[3:6]} - {a[6:10]}"
    return "Invalid phone number"


print(format_phone_number("555-123-4567"))  # (555) - 123 - 4567
print(format_phone_number("(555) 123 4567"))  # (555) - 123 - 4567
print(format_phone_number("5551234567"))  # (555) - 123 - 4567
print(format_phone_number("123"))  # Invalid phone number
