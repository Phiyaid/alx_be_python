def perform_operation(num1, num2, operation):
    
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide": 
            return num1 / num2
        else:
            print("Enter a valid operation")
    except ZeroDivisionError : return 1