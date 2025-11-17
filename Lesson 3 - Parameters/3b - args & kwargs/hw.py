# Question 1
def combine_values(*values):
    if not values:
        return 1
    product = 1
    for v in values:
        product *= v
    return product


print(combine_values(2, 3, 4))  # 24
print(combine_values(5))  # 5
print(combine_values())  # 1
print()


# Question 2
def merge_details(label, **info):
    result = {"label": label}
    result.update(info)
    return result


print(merge_details("ItemA", size="Large", cost=12.50))
# {"label": "ItemA", "size": "Large", "cost": 12.50}
print(merge_details("UserX"))  # {"label": "UserX"}


# Question 3
# 8
# 10
# 0


# Question 4
# {'name': 'Alpha', 'x': 1, 'y': 2, 'count': 2}
# {'name': 'Beta', 'count': 0}
