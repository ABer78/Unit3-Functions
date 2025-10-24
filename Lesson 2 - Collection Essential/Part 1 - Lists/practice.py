def filter_evens(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


print(filter_evens([1, 2, 3, 4]))  # [2, 4]


def list_stats(numbers):
    if numbers:
        minimum = min(numbers)
        maximum = max(numbers)
        total = sum(numbers)
        avg = total / len(numbers)
        return (minimum, maximum, avg)
    return None


print(list_stats([5, 10, 15, 20]))  # (5, 20, 12.5)
print(list_stats([]))  # None
