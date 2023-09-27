def is_even(number):
    return number % 2 == 0

num = 6

if is_even(num):
    print(f"{num} является четным.")
else:
    print(f"{num} не является четным.")