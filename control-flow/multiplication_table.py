number = int(input("Enter a number to see its multiplication tables: "))

for item in range(1, 11):
    product = int(number) * item
    print(f"{number} * {item} = {product}")