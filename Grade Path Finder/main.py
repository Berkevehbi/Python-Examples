from typing import List


def calculate_gpa(course_content: List) -> float:
    """
    This function calculates and returns gpa.
    """
    letter_note = {
        "A1": 4.00, "A2": 3.75, "A3": 3.50,
        "B1": 3.25, "B2": 3.00, "B3": 2.75,
        "C1": 2.50, "C2": 2.25, "C3": 2.00,
        "D": 1.75
    }
    total = 0
    total_credit = 0
    for course in course_content:
        credit = course[0]
        grade = course[1]

        total += letter_note[grade] * credit
        total_credit += credit

    return round(total / total_credit, 2)


def check_all_notes_given(course_content: List) -> bool:
    """
    Checks if all grades for course content are valid.
    """
    letter_note = {
        "A1": 4.00, "A2": 3.75, "A3": 3.50,
        "B1": 3.25, "B2": 3.00, "B3": 2.75,
        "C1": 2.50, "C2": 2.25, "C3": 2.00,
        "D": 1.75
    }
    for i in range(len(course_content)):
        grade = course_content[i][1]

        if not (grade in letter_note):
            return False
    return True


def find_e(course_content: List) -> int:
    """
    Returns the index when it finds the letter grade "E" in the course_content list.
    """
    for i in range(len(course_content)):
        grade = course_content[i][1]

        if grade == "E":
            return i

    return -1


def calculate(course_content: List, target_grade: float, paths: List, current_path=None) -> bool:
    """
        Recursively calculates possible paths to achieve the target grade considering letter grades.

        This function recursively explores different combinations of letter grades in 'course_content'
        to achieve the 'target_grade'. It replaces the grade of the current course with each possible
        letter grade and recursively calls itself until it reaches the base case where no more courses
        are left. If the GPA matches the 'target_grade', it appends the path to 'paths' and returns True.
        If no valid path is found, it returns False.
        """
    letter_note = [
        ["A1", 4.00], ["A2", 3.75], ["A3", 3.50],
        ["B1", 3.25], ["B2", 3.00], ["B3", 2.75],
        ["C1", 2.50], ["C2", 2.25], ["C3", 2.00],
        ["D", 1.75]
    ]
    i = find_e(course_content)

    if i == -1:
        if calculate_gpa(course_content) == target_grade:
            paths.append(current_path)
            return True
        else:
            return False

    original_grade = course_content[i][1]

    found = False
    for letter in letter_note:
        course_content[i][1] = letter[0]
        new_path = current_path + [letter[0]] if current_path else [letter[0]]
        if calculate(course_content, target_grade, paths, new_path):
            found = True
    course_content[i][1] = original_grade

    return found


def find_all_paths(course_content: List, target_grade: float):
    """
        Finds all possible paths to achieve the target grade considering letter grades.

        This function initializes an empty list 'paths', then uses the 'calculate' function
        to find all possible paths that lead to achieving the 'target_grade' based on the
        letter grades. It returns a list containing all these possible paths.
        """
    paths = []
    calculate(course_content, target_grade, paths)
    return paths


def main():
    course_credits = {}

    # Here we get course names and credits from the user.
    while True:
        course_name = input("Enter your course name (If you have nothing else to write, type Done): ")
        if course_name.lower() == "done":
            break
        course_credit = int(input("Enter your course credit: "))
        course_credits[course_name] = course_credit

    course_content = []

    # Here we give all subjects an E grade.
    # The reason why it is E is so that it does not contain any letters from the letter grade.
    for course_name, credit in course_credits.items():
        course_content.append([credit, "E", course_name])

    target_grade = float(input("What is your target grade: "))

    # This is where the real loop starts
    all_paths = find_all_paths(course_content, target_grade)
    if all_paths:
        print("Possible paths to reach the target grade:")
        for path in all_paths:
            course_notes = []
            for i, note in enumerate(path):
                course_notes.append(f"{course_content[i][2]}: {note}")
            print(", ".join(course_notes))
    else:
        print("No paths found to reach the target grade.")


if __name__ == "__main__":
    main()
