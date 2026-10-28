print("#--------CALCULATOR--------#")
while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Average")
    print("6.Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("-----------------------------------------------------")
        print("Invalid input! Please enter a number for the choice.")
        continue

    if choice == 6:
        print("\nThank you for using")
        break
    # Check if the choice is valid BEFORE asking for numbers
    if choice not in[1,2,3,4,5,6]:
        print("-----------------------------------------------------")
        print("Invalid choice! Please enter a right value from the menu.")
        continue
    # Ask for inputs only if the choice is valid
    try:
        num_1 = int(input("Enter first number"))
        num_2 = int(input("Enter second number"))
    except ValueError:
        print("Invalid input! please enter numbers only")
        continue
    match choice:
        case 1:
            print("-----------------------------------------------------")
            print(f"Sum of number {num_1} and {num_2} is {num_1 + num_2} ")
        case 2:
            print("-----------------------------------------------------")
            print(f"Difference of number {num_1} and {num_2} is {num_1 - num_2} ")
        case 3:
            print("-----------------------------------------------------")
            print(f"product of number {num_1} and {num_2} is {num_1 * num_2} ")
        case 4:
            print("-----------------------------------------------------")
            if num_2 != 0:
                print(f"Division of number {num_1} and {num_2} is {num_1 / num_2:.2f} ")
            else:
                print("Error:Division is not possible ")
        case 5:
            print("-----------------------------------------------------")
            print(f"Average of number {num_1} and {num_2} is {(num_1 + num_2)/2} ")
        
                                                        
        
