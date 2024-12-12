
def task_number(task_num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Task {task_num}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@task_number(1)
def display_quote():
    print("“Don’t compare yourself with anyone in this world…")
    print(" if you do so, you are insulting yourself.”")
    print("\t\t\t\t\t\t\t\t\tBill Gates")

@task_number(2)
def display_even_numbers(start, end):
    for num in range(min(start, end) + 1, max(start, end)):
        if num % 2 == 0:
            print(num, end=" ")
    print()

@task_number(3)
def display_square(side_length, symbol, filled):
    for i in range(side_length):
        if filled or i == 0 or i == side_length - 1:
            print(symbol * side_length)
        else:
            print(symbol + " " * (side_length - 2) + symbol)

@task_number(4)
def find_minimum(a, b, c, d, e):
    return min(a, b, c, d, e)

@task_number(5)
def calculate_product_in_range(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product

@task_number(6)
def count_digits(number):
    return len(str(abs(number)))

@task_number(7)
def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

if __name__ == "__main__":
    # Завдання 1
    display_quote()

    # Завдання 2
    display_even_numbers(2, 10)

    # Завдання 3
    display_square(5, "*", True)
    display_square(5, "*", False)

    # Завдання 4
    print(find_minimum(3, 5, 1, 7, 2))

    # Завдання 5
    print(calculate_product_in_range(5, 1))

    # Завдання 6
    print(count_digits(3456))

    # Завдання 7
    print(is_palindrome(123321))
    print(is_palindrome(421987))
