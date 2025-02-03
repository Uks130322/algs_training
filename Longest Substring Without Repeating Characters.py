# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(self, s: str) -> int:
    begin = 0
    end = 0
    longest = 0
    chars = dict()
    for i, char in enumerate(s):
        end = i
        if char in chars:
            begin = max(begin, chars[char] + 1)
            end = max(end, begin)
        longest = max(longest, end - begin + 1)
        chars[char] = i
    return longest