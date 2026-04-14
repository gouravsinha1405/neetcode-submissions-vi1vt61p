import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r"[^A-Za-z0-9]","",s)

        return (s.lower() == s[::-1].lower())

        