# Requirement
# Take user input for the grade
# 90 – 100 A
# 80 – 89 B
# 70 – 79 C
# 60 – 69 D
# Below 60 E

class InvalidMarkError(Exception):
    """Raised when the mark is invalid"""
    pass

def check_grade(mark):
    if (mark > 100) | (mark < 0):
        raise InvalidMarkError("Mark should be within 0 - 100 only.")
    elif mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"
    return grade

try:
    mark = int(input("Enter your mark (0-100): "))
    grade = check_grade(mark)
except Exception as e:
    print(f"An error occurred {e}")
else:
    print(f"Mark: {mark} -> Grade: {grade}")