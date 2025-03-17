def factorial_while(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


number = int(input("Please enter a number: "))
print(factorial_while(number))
    