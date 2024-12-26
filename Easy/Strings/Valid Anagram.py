class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)
        if len(counter_s) != len(counter_t):
            return False

        for k in counter_s:
            if counter_t[k]:
                if counter_s[k] != counter_t[k]:
                    return False
            else:
                return False
        return True