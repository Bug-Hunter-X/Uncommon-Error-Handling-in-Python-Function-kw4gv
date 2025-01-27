def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError if a is 0
    elif b == 0:
        return a / b # ZeroDivisionError if b is 0
    else:
        return a + b

result = function_with_uncommon_error(0, 5)
print(result)  # Raises ZeroDivisionError