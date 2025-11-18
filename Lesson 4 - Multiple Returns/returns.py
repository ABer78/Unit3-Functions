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
