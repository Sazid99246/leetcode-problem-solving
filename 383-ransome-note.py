from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = dict(Counter(ransomNote))
        magazineCounter = dict(Counter(magazine))

        for k, v in ransomNoteCounter.items():
            if magazineCounter.get(k, 0) < v:
                return False
        return True
