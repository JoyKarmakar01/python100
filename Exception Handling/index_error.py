def access_list_element():
    try:
        numbers = [10, 20, 30, 40, 50]
        index = int(input("Enter an index (0-4): "))
        print(f"✅ Element at index {index}: {numbers[index]}")
    except IndexError:
        print("⚠️ Error: Index out of range! Choose between 0 and 4.")
    except ValueError:
        print("⚠️ Error: Invalid input! Enter a number.")

access_list_element()
