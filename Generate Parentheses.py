# https://leetcode.com/problems/generate-parentheses/description/


def generateParenthesis(self, n: int) -> list[str]:
    if n == 0:
        return []
    result = ['()']
    for i in range(n - 1):
        new_result = set()
        for item in result:
            for i in range(len(item)):
                new_result.add(item[:i] + '()' + item[i:])
        result = list(new_result)

    return result


print(generateParenthesis(0, 2))
print(generateParenthesis(0, 3))