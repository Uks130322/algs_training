# https://leetcode.com/problems/spiral-matrix-ii/description/


def generateMatrix(self, n: int) -> list[list[int]]:
    matrix = [[None] * n for _ in range(n)]
    i = 0
    j = 0
    direction = 1
    for num in range(1, n * n + 1):
        matrix[i][j] = num
        if direction == 1:
            j += 1
            if j < n and matrix[i][j] is None:
                continue
            else:
                j -= 1
                direction = 2
        if direction == 2:
            i += 1
            if i < n and matrix[i][j] is None:
                continue
            else:
                i -= 1
                direction = 3
        if direction == 3:
            j -= 1
            if j >= 0 and matrix[i][j] is None:
                continue
            else:
                j += 1
                direction = 4
        if direction == 4:
            i -= 1
            if i >= 0 and matrix[i][j] is None:
                continue
            else:
                i += 1
                j += 1
                direction = 1

    return matrix


print(generateMatrix(0, 2))