def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
   
    # Read two numbers from user input given from console
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = add_two_numbers(a, b)
    # Print as int if both inputs were integers (optional)
    if result.is_integer():
        print(int(result))
    else: 
        print(result)





