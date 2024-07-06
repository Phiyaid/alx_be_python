def perform_operation(num1, num2, operation):
    
    try:
        match operation:
            case "add": return chosen = num1 + num2
            case "subtract": return chosen = num1 - num2
            case "multiply": return chosen = num1 * num2
            case "divide": return chosen = num1 / num2
    except ZeroDivisionError : return 1