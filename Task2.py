import math

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("side length must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("sides don't form a valid triangle")
    
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

def course_result(coursework, final, attendance):
    total = coursework + final
    if attendance >= 0.75 and final >= 30 and total >= 60:
        return "Pass"
    else:
        return "Fail"

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_below(n):
    return [i for i in range(2, n) if is_prime(i)]


def first_repeated(values):
    for i in range(len(values)):
        if values[i] in values[:i]:
            return values[i]
    return None


def count_pairs(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2


def calculator(command):
    match command.split():
        case [a, "+", b]:
            return float(a) + float(b)
        case [a, "-", b]:
            return float(a) - float(b)
        case [a, "*", b]:
            return float(a) * float(b)
        case [a, "/", b]:
            return float(a) / float(b)
        case _:
            raise ValueError("Invalid command format")


def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default


def stats(*numbers):
    if not numbers:
        return None
    
    min_val = numbers[0]
    max_val = numbers[0]
    total = 0
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        total += num
        
    avg = total / len(numbers)
    return min_val, max_val, avg


def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target


def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier


def apply_n(f, x, n):
    result = x
    for _ in range(n):
        result = f(result)
    return result


