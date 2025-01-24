def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        print(s[left], left,  s[right], right)
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() == s[right].lower():
            print('here')
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome(0, 'race a car'))