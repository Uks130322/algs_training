# 281 Zigzag Iterator


def zigzag(v1: list[int], v2: list[int]) -> list[int]:
    length = min(len(v1), len(v2))
    result = []
    for i in range(length):
        result.append(v1[i])
        result.append(v2[i])
    result += v1[length:]
    result += v2[length:]
    return result


print(zigzag(v1 = [1, 2], v2 = [3,4]))
