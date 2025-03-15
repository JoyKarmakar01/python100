def multiple_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        numbers = [1, 2, 3]
        print(f"✅ List value: {numbers[num]}")  # Might cause IndexError
    except ZeroDivisionError:
        print("⚠️ Error: Division by zero is not allowed!")
    except ValueError:
        print("⚠️ Error: Invalid input! Please enter a number.")
    except IndexError:
        print("⚠️ Error: Index out of range!")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

multiple_exceptions()
