def sum_digits(number):
    number_str = str(number)
    
    total = 0
    
    for digit in number_str:
        total += int(digit)
    
    return total

number = 12345

digit_sum = sum_digits(number)
print(f"Сумма цифр числа {number} равна {digit_sum}")