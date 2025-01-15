class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                pref += char[0]
            else:
                break
        return pref
