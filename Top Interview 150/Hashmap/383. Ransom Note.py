class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = Counter(magazine)
        count_ran = Counter(ransomNote)
        for k in count_ran:
            if count_mag[k] < count_ran[k]:
                return False
        return True