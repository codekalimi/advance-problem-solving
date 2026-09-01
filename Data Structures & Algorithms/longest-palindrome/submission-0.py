class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_length = 0
        c_count = {}
        for c in s:
            c_count[c] = c_count.get(c, 0) + 1
            if c_count[c] % 2 == 0:
                max_length += 2
        for count in c_count.values():
            if count % 2 != 0:
                max_length +=1
                break
        return max_length 