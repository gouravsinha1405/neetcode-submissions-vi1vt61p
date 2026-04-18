class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = {}
        start = 0
        max_count = 0
        for end in range(len(s)):

            dupes[s[end]] = dupes.get(s[end], 0)+1

            while dupes[s[end]] > 1:
                dupes[s[start]] -= 1
                start += 1
            max_count = max(max_count, end-start+1)
        return max_count


        


        