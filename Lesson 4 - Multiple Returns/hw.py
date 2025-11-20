# Question 1
def search_user_database(query):
    if not query or query.strip() == "":
        return None, "No search query", False
    if not query.isalpha():
        return False, "Invalid characters", False
    if query.lower() in ["admin", "user", "guest"]:
        return 0, "No users found", True
    elif query.lower() in ["john", "jane", "bob"]:
        return 3, "Found 1 user", True


# Test Case 1:
result, message, success = search_user_database("")
print(result)  # None
print(message)  # "No search query"
print(success)  # False
print()

# Test Case 2:
result, message, success = search_user_database(" ")
print(result)  # None
print(message)  # "No search query"
print(success)  # False
print()

# Test Case 3:
result, message, success = search_user_database("user123")
print(result)  # False
print(message)  # "Invalid characters"
print(success)  # False
print()


# Question 2
def analyze_book_pages(page_count):
    if not page_count:
        return 0, 0, 0.0, False
    book_count = len(page_count)
    total_pages = sum(page_count)
    average = total_pages / book_count
    has_long_book = max(page_count) > 500

    return book_count, total_pages, average, has_long_book


# Test Case 1:
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count)  # 4
print(total)  # 1360
print(avg)  # 340.0
print(has_long)  # True
print()

# Test Case 2:
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count)  # 3
print(total)  # 650
print(avg)  # 216.66666666 . . .
print(has_long)  # False
print()

# Test Case 3:
count, total, avg, has_long = analyze_book_pages([])
print(count)  # 0
print(total)  # 0
print(avg)  # 0.0
print(has_long)  # False
print()
