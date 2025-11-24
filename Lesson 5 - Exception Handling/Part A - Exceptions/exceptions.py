def safe_divide(a, b):
    try:
        result = a / b
        return result
    # except:
    #     print("Can not divide by zero")
    #     return None
    except ZeroDivisionError:
        print("Can not divide by zero")
        return None
    except TypeError:
        print("That's not a valid number")
        return None
    except:
        print("An error has occured . . .")


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Can not divide by zero (on the next line): None
print(safe_divide(10, "hello"))  # That's not a valid number (on the next line): None
print()


def safe_operation(a, b, lst, key, d):
    try:
        print(f"Division Result: {a/b}")  # ZeroDivisionError; TypeError
        print("Access List Element", lst[2])  # Index Error
        print("Access Dictionary Key", d[key])  # Key Error
        print("Add Numbers", {a + b})  # Type Error
    except ZeroDivisionError:
        print("Can not divide by zero")
    except IndexError:
        print("List index is out of reach")
    except KeyError:
        print(f"Key {key} not found in dictionary")
    except TypeError:
        print("Invalid types for operation")
    except Exception as e:
        print("Some other error occured", e)


print(safe_operation(10, 2, [1, 2], "Tom", {"John": 15}))
# Division Result: 5.0 (on the next line): List index is out of reach (on the next line): None
print(safe_operation(10, 0, [1, 2], "Tom", {"John": 15}))
# Can not divide by zero (on the next line): None
print(safe_operation(10, "hello", [1, 2], "Tom", {"John": 15}))
# That's not a valid number (on the next line): None
print()


def calculate_price_per_item(total_cost, num_items):
    try:
        price = total_cost / num_items
        return round(price, 2)
    except:
        print("An error has occured")


print(calculate_price_per_item(25, 3))  # 8.33
print(calculate_price_per_item(37, 2))  # 18.5
print(calculate_price_per_item(25.50, 1))  # 25.5
print()


def parse_age(age):
    try:
        return int(age)
    except ValueError:
        return None

print(parse_age(3)) # 3
print(parse_age("three")) # None
print(parse_age(-2)) # -2
print(parse_age(2.5)) # 2
print()


