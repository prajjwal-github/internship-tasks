# Student Grade Calculator
# This program takes student marks and returns grade with encouraging messages

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep it up!"
    elif marks >= 75:
        return "B", "Great job! You are doing really well."
    elif marks >= 60:
        return "C", "Good effort! You can do even better."
    elif marks >= 40:
        return "D", "You passed. Keep practicing and improving."
    else:
        return "F", "Don't be discouraged. Learn from mistakes and try again."

def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0 - 100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

def main():
    print("Student Grade Calculator")
    print("------------------------")

    name = input("Enter student name: ").strip()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\nResult")
    print("------")
    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()