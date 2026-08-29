class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        if not strs:
            return longest
        first = strs[0]
        for i in range(len(first)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first[i]:
                    return longest
            longest += first[i]
        return longest