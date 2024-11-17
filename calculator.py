def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    result = None
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result is: {result}")

    elif operator == "/":
        if num1 == 0 or num2 == 0 :
         print("divide by 0 is not posssible")
        else :
            result = num1 / num2
            print(f"The result is: {result}")

    elif operator == "%":
        result = num1 % num2
        print(f"The result is: {result}")

    elif operator == ">":
        if num1 > num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == ">=":
        if num1 >= num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == "<":
        if num1 < num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == "<=":
        if num1 <= num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")
    else:
        print("Invalid operator.")

    return result

## Run the example
# calculator(4, 5, "*")  # Output: The result is: 20
# calculator(10, 2, "/")  # Output: The result is: 5.0
# calculator(7, 7, ">=")  # Output: The comparison result is: True

#calculator(4, 5, "*")
#calculator(10, 2, "/")
#calculator(9, 5, "-")
#calculator(12, 3, "+")
#calculator(7, 7, ">=")
#calculator(456, 2, "*")
#calculator(100, 0, "/")
#calculator(-9, 5, "-")
#calculator(-34, -3, "+")
#calculator(63, -9, ">=")

