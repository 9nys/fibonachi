def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(5)
print("Результат обчислення числа Фібоначчі:", result)