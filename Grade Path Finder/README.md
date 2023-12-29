# Grade Path Finder

This project aims to find possible paths to achieve a target GPA using backtracking algorithms. The motivation behind this project is to better understand recursive functions and gain a deeper comprehension of the backtracking method.

## Project Overview

The Grade Path Finder script utilizes backtracking to explore various combinations of letter grades within a course curriculum to reach a specified target GPA. It enables users to input course details (names, credits) and a target GPA. The script then computes the necessary letter grades per course to attain the target GPA.

## Using the Backtracking Method

The project employs backtracking as follows:

1. **Recursive Calculation:**
   - The `calculate()` function recursively explores different combinations of letter grades to achieve the target GPA. It replaces the grade of the current course with each possible letter grade and calls itself until it reaches the base case where no more courses are left.

2. **Path Exploration:**
   - It tracks and records paths that lead to reaching the target GPA. If a valid path matches the target GPA, it appends the path to the list of possible paths.

## How to Use

1. **Python Environment:**
   - Requires Python 3.

2. **Usage:**
   - Run the terminal
   - Type this: python main.py

## Example Usage
To run the program, navigate to the project directory in the terminal:

```bash
python main.py


Enter your course name (If you have nothing else to write, type Done): Math
Enter your course credit: 5

Enter your course name (If you have nothing else to write, type Done): Physic
Enter your course credit: 4

Enter your course name (If you have nothing else to write, type Done): Introduction to Programming
Enter your course credit: 3

Enter your course name (If you have nothing else to write, type Done): Done

What is your target grade: 3.4

Possible paths to reach the target grade:

Math: A1, Physic: A3, Introduction to Programming: C2
Math: A1, Physic: B3, Introduction to Programming: B1
Math: A2, Physic: A1, Introduction to Programming: C3
Math: A2, Physic: B1, Introduction to Programming: B2
Math: A2, Physic: C1, Introduction to Programming: A1
Math: A3, Physic: A2, Introduction to Programming: B3
Math: A3, Physic: B2, Introduction to Programming: A2
Math: B1, Physic: A3, Introduction to Programming: A3
Math: B2, Physic: A1, Introduction to Programming: B1
Math: B3, Physic: A2, Introduction to Programming: A1
```

### Project Motivation
The "Grade Path Finder" project emerged as a quest to deepen my grasp of recursive algorithms and the practical application of backtracking. By creating a tool to compute required letter grades for a target GPA, I aim to explore these fundamental concepts hands-on. This project isn't just about finding solutions but about unraveling the intricacies of recursive thinking and problem-solving methodologies.


