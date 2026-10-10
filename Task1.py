# 1
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# 2
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


# 3
def split_evenly(total, people):
    each = total // people
    remainder = total % people

    return each, remainder


# 4
def initials(full_name):
    parts = full_name.split()
    result = ""

    i = 0
    while i < len(parts):
        result += parts[i][0].upper()
        i += 1

    return result


# 5
def is_palindrome_word(word):
    word = word.strip().lower()
    return word == word[::-1]


# 6
def mask_email(email):
    at = email.index("@")

    name = email[:at]
    domain = email[at:]

    if len(name) <= 2:
        masked_name = name[0] + "*"
    else:
        masked_name = name[0] + ("*" * (len(name) - 2)) + name[-1]

    return masked_name + domain


# 7
def middle(values):
    n = len(values)

    if n % 2 == 1:
        return values[n // 2]
    else:
        return values[n // 2 - 1:n // 2 + 1]


# 8
def rotate_left(values, k):
    n = len(values)

    if n == 0:
        return []

    k = k % n

    return values[k:] + values[:k]


# 9
def fib_list(n):
    result = []

    a = 0
    b = 1

    i = 0
    while i < n:
        result.append(a)
        a, b = b, a + b
        i += 1

    return result


# 10
def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps
