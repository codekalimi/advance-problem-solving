class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words = {}
        for ch in s:
            if ch in words:
                words[ch] += 1
            else:
                words[ch] = 1
        for ch in t:
            if ch in words and words[ch] >0:
                words[ch] -= 1
            else:
                return False
        return True