n = int(input("Enter how many rows of Pascal's Triangle you want to print: "))

def create_pascal_triangle(n):
    pascal_list = []
    for i in range(n):
            temp_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    temp_list.append(pascal_list[i - 1][j] + pascal_list[i - 1][j - 1])
            pascal_list.append(temp_list)
    return pascal_list

pascal_list = create_pascal_triangle(n)


def print_pascal_triangle(pascal_list):
    max_width = len(" ".join(map(str, pascal_list[-1])))
    for row in pascal_list:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

print_pascal_triangle(pascal_list)
"""
for a in range(len(pascal_list)):
    for i in range(len(pascal_list) - a - 1):
        print(" ", end="")
    for j in range(len(pascal_list[a])):
        print(pascal_list[a][j]," ",end="",sep="")
    for k in range(len(pascal_list) - a - 2):
        print(" ",end="")
    print()
"""