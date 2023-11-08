def create_pascal_triangle(n):
    """
    Function to generate a Pascal's triangle as a list.

    Args:
        n (int): The number of rows in the Pascal's triangle to create.

    Returns:
        list: A list representing Pascal's triangle. Each row is stored as a sub-list.
              For example, for n=3, the result would be:
              [[1], [1, 1], [1, 2, 1]]
    """
    pascal_list = []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                # If we are at the beginning or end of the triangle, we need to append 1 because of the Pascal's triangle rule.
                temp_list.append(1)
            else:
                # If we are somewhere in the middle, we need to append the top row by adding the current column and the previous column.
                temp_list.append(pascal_list[i - 1][j] + pascal_list[i - 1][j - 1])
        pascal_list.append(temp_list)
    return pascal_list

def print_pascal_triangle(pascal_list):
    """
    Print Pascal's triangle with proper formatting.

    Args:
        pascal_list (list): A list representing Pascal's triangle. Each row should be stored as a sub-list.

    Returns:
        None

    This function takes a Pascal's triangle represented as a list and prints it to the console. 
    The rows of the triangle are centered and properly formatted to create an easily readable output.
    """
    if len(pascal_list) == 0:
        # If the length of pascal_list is equal to zero, either a negative number or 0 is given as input. In this case there is no pascal triangle. 
        print("Negative number and 0 can not be acceptable.")
        return
    # Here we take the longest line, convert it to a string with the map function and measure the length of the bottom line with a space between them.
    max_width = len(" ".join(map(str, pascal_list[-1])))
    for row in pascal_list:
        # Here, we turn the line we are processing into a string with the map function and turn the whole line into a string by leaving spaces with the join function.
        row_str = " ".join(map(str, row))
        # Here we print the line centered on the largest length.
        print(row_str.center(max_width))

"""

I wrote this function for the first time while trying to write a Pascal triangle, but it gives a garbled output. 
Because instead of centering it leaves as many spaces as how many sub-rows it has. 
This is incorrect because after a certain point the numbers become 2, 3... digits and the balance becomes unbalanced.

for a in range(len(pascal_list)):
    for i in range(len(pascal_list) - a - 1):
        print(" ", end="")
    for j in range(len(pascal_list[a])):
        print(pascal_list[a][j]," ",end="",sep="")
    for k in range(len(pascal_list) - a - 2):
        print(" ",end="")
    print()
"""

n = int(input("Enter how many rows of Pascal's Triangle you want to print: "))

pascal_list = create_pascal_triangle(n)
print_pascal_triangle(pascal_list)
