class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        last_counter = 0
        #count vowels in the firs sub
        for i in s[:k]:
            if i in ['a', 'e', 'i', 'o', 'u']:
                last_counter += 1
        max_counter = last_counter
        #now check the others
        for c in range(len(s)-k):
            if s[c] in ['a', 'e', 'i', 'o', 'u']:
                last_counter -= 1
            if s[c+k] in ['a', 'e', 'i', 'o', 'u']:
                last_counter += 1
            max_counter = max(max_counter,last_counter)
        return max_counter