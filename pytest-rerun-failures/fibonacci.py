def fibonacci(n):
    result = 0
    
    if (n <= 1):
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    return result
