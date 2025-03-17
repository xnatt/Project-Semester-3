def factorial_for(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


number = int(input("Please enter a number: "))
print(factorial_for(number))
    