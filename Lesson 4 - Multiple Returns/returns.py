def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)


# Return Type 1 - None -> "No Value"
# Meaning: absense of value, not set, not found
# Use for: missing data, search failures, optional parameters
result = None
print(result is None)  # True; identity check
print(result == None)  # True; equality check
print(not result)  # True; falsy check
print()

# Return Type 2 - False -> Boolean False
# Meaning: explicit false condition, validation failure, negative
# Use for: validation result, boolean operations, success/failure status
result = False
print(result is False)  # True; identity check
print(not result)  # True; boolean negation
print(result == 0)  # True; falsy check
print()

# Return Type 3 - 0 -> A Valid Number
# Zero is a valid numeric value, not an absense in value
result = 0
print(result == 0)  # True; numeric equality
print(not result)  # True; (falsy in boolean context)
print(result is None)  # False; different objects
print(result is False)  # False; different types


# Multiple Returns - python packs multiple returns into a tuple:
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  #


result = calculate_room(10, 5)
print(result)  # (50, 30)
print(type(result))  # <class 'tuple'>
print(type(42))  # <class 'int'>
print(
    type(
        42,
    )
)  # <class 'int'>
no_parenthesis = 1, 2, 3
print(type(no_parenthesis))  # <class 'tuple'>
print()


# Unpacking tuple
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}")  # 120
print(f"Perimeter: {perimeter_result}")  # 52
print()


def analyze_grades(grades):
    if not grades:
        return 0, 0, 0, False
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 68
    return average, highest, lowest, passed


result = analyze_grades([85, 96, 83, 90])
print(result)  # (88.5, 96, 83, True)
