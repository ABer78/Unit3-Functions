# Question 15
# the function does not check if the list is empty, causing a ZeroDivisionError

# Question 16
# C - required, *args, defaults, **kwargs

# Question 17
# strip
# upper
# split
# len


# Question 18
def validate_password(password):
    if not password:
        return False, "Empty password"
    if len(password) < 8:
        return False, "Too short"
    return True, "Valid"


print(validate_password(""))  # (False, 'Empty password')
print(validate_password("abc"))  # (False, 'Too short')
print(validate_password("secure123"))  # (True, 'Valid')
print()


# Question 19
def create_inventory(item_name, *quantities, location="Warehouse"):
    total = sum(quantities) if quantities else 0
    return {
        "item": item_name,
        "total": total,
        "location": location,
    }


print(create_inventory("Widget", 10, 20, 15))
# {'item': 'Widget', 'total': 45, 'location': 'Warehouse'}
print(create_inventory("Gadget", 5, location="Store"))
# {'item': 'Gadget', 'total': 5, 'location': 'Store'}
print()


# Question 20
def safe_list_access(items, index):
    try:
        value = items[index]
        return value, True
    except IndexError:
        return None, False


print(safe_list_access([10, 20, 30], 1))  # (20, True)
print(safe_list_access([10, 20, 30], 10))  # (None, False)
print(safe_list_access([], 0))  # (None, False)
