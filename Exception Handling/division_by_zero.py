def divide_numbers():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print(f"✅ Result: {result}")
    except ZeroDivisionError:
        print("⚠️ Error: Cannot divide by zero!")
    except ValueError:
        print("⚠️ Error: Invalid input! Please enter numbers only.")

divide_numbers()
