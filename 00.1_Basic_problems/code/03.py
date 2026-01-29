# check whether a number is palindrome or not

def isPalindrome(x: int) -> bool:
        original = x
        reverse = 0

        while x > 0:
            reverse = reverse * 10 + x%10
            x//=10
        return original == reverse


# print(isPalindrome(121))  # Example usage


# Check whether a string is palindrome or not
def isPalindrome(s: str) -> bool:
        st = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(st) - 1

        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        return True

print(isPalindrome("A man, a plan, a canal: Panama"))

import re
def isPalindrome(s: str) -> bool:
        cleaned_st = re.sub(r'[^a-zA-Z0-9]', '', s)
        return cleaned_st.lower() == cleaned_st[::-1].lower()

print(isPalindrome("A man, a plan, a canal: Panama"))

