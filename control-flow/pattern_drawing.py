number  = int(input("Enter the size of the pattern: "))

while number <= 0:
    number  = int(input("Enter the size of the pattern: "))
    
num_of_asteriks = number

while number != 0:
    for i in range(num_of_asteriks):
        print("*", end = "")
    number -=1
    print("")