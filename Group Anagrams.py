# https://leetcode.com/problems/group-anagrams/description/


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    words_dict = dict()
    for word in strs:
        sorted_word = sorted(word)
        new_word = ''
        count = 1
        for letter in sorted_word:
            if not new_word or new_word[-1] != letter:
                new_word += letter + str(count)
                count = 1
            else:
                count += 1
        words_dict[new_word] = words_dict.get(new_word, []) + [word]
    return list(words_dict.values())


print(groupAnagrams(1, ["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(1, [""]))