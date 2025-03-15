def search_dictionary():
    try:
        student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
        name = input("Enter student name: ").strip()
        print(f"✅ {name}'s score: {student_scores[name]}")
    except KeyError:
        print("⚠️ Error: Student not found! Check the spelling.")

search_dictionary()
