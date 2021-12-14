# Source:https://www.xarg.org/puzzle/project-euler/problem-28/
def sum_diagonals(size):
    # We must remove the middle element (and require an odd number)
    # and divide by two since we need only half of the diagonal.
    n = int((size - 1) / 2)
    sum = 1
    for i in range(1, n + 1):
        a_diagonal = 4 * (i * i) + 4 * i + 1  # 9,25,49,81,121...
        b_diagonal = 4 * (i * i) + 1  # 5,17,37,65,101...
        c_diagonal = 4 * (i * i) - 2 * i + 1  # 3,13,31,57,91...
        d_diagonal = 4 * (i * i) +  2 * i + 1  # 7,21,43,73,111...
        sum += a_diagonal + b_diagonal + c_diagonal + d_diagonal
    return sum


print(sum_diagonals(1001))
