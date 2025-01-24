# https://leetcode.com/problems/string-compression/


def compress(self, chars: list[str]) -> int:
    count = 1
    short = [chars[0]]
    prev = chars[0]
    for char in chars[1:]:
        if char == prev:
            count += 1
        elif count == 1:
            short.append(char)
            prev = char
        else:
            short += list(str(count))
            short.append(char)
            count = 1
            prev = char
    if count > 1:
        short += list(str(count))
    result = len(short)
    chars[:result] = short
    return result


print(compress(0, ["a","a","b","b","c","c","c"]))
