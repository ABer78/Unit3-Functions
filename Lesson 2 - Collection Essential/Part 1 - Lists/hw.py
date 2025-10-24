# Problem 1:
def remove_duplicates(items):
    improved = []
    for item in items:
        if item not in improved:
            improved.append(item)
    return improved


print(remove_duplicates([1, 2, 2, 3]))  # [1, 2, 3]
print()


# Problem 2:
def find_common(list1, list2):
    common = []
    for items1 in list1:
        for items2 in list2:
            if items1 == items2:
                common.append(items1)
    return common


print(find_common([1, 2, 3], [2, 3, 4]))  # [2, 3]
print()


# Problem 3:
def reverse_sublists(data, size):
    inverted = []
    for i in range(0, len(data), size):
        chunk = data[i : i + size]
        inverted.extend(chunk[::-1])
    return inverted


print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))  # [2, 1, 4, 3, 6, 5]
print(reverse_sublists([1, 2, 3, 4, 5], 3))  # [3, 2, 1, 5, 4]
print(reverse_sublists([1, 2, 3, 4], 1))  # [1, 2, 3, 4]
print(reverse_sublists([1, 2, 3], 5))  # [3, 2, 1]
print()


# Problem 4:
def rotate_lists(items, position):
    n = len(items)
    position = position % n
    return items[-position:] + items[:-position]


print(rotate_lists([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(rotate_lists([1, 2, 3, 4, 5], -2))  # [3, 4, 5, 1, 2]
print(rotate_lists([1, 2, 3], 0))  # [1, 2, 3]
print(rotate_lists([1, 2, 3], 5))  # [2, 3, 1]
