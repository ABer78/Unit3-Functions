# announcement = " BERGEN TECH robotics meeting TODAY! "


def format_course_code(code):
    trimmed = code.strip()
    formatted = trimmed.upper()
    return f"'{formatted}'"
    # return code.strip().upper()


print(format_course_code(" Hello "))
print(format_course_code("machine "))


def count_hashtags(post):
    split = post.split()
    count = 0

    for word in split:
        if word.startswith("#"):
            count += 1
    return count


post1 = "Great game today! #BergenTech #GoGamrz #Pride"
print(count_hashtags(post1))


def pdf_checking(file):
    status = False
    if file.endswith(".pdf"):
        status = True
    return status


print(pdf_checking("pythoncode.pdf"))  # True
print(pdf_checking("pythoncode"))  # False
