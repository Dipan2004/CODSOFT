import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    while True:
        clear_screen()
        print("\t*** Simple Calculator ***")
        
        # Input first number
        while True:
            try:
                num1 = float(input("\nEnter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Input operation
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        while True:
            choice = input("\nEnter the operation number (1-5): ")
            if choice in ['1', '2', '3', '4', '5']:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        # Input second number
        while True:
            try:
                num2 = float(input("\nEnter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Perform calculation
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
                input("\nPress Enter to continue...")
                continue
            result = num1 / num2
            operation = '/'
        
        # Display result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    calculator()