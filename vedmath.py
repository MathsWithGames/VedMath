def nikhilam(a, b):
    base = 100

    da = base - a
    db = base - b

    left = a - db
    right = da * db

    answer = left * base + right

    return answer
print(__name__)