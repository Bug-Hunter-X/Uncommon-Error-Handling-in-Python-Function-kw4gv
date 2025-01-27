def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b / a
        elif b == 0:
            return a / b
        else:
            return a + b
    except ZeroDivisionError:
        return "Error: Division by zero"

result = function_with_uncommon_error(0, 5)
print(result)  # Prints "Error: Division by zero"

result2 = function_with_uncommon_error(5,0)
print(result2) # Prints "Error: Division by zero"

result3 = function_with_uncommon_error(5,2)
print(result3) # Prints 7