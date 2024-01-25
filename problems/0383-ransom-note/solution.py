class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteFreq = Counter(ransomNote)
        magazineFreq = Counter(magazine)

        for k, v in ransomNoteFreq.items():
            if magazineFreq[k] < ransomNoteFreq[k]:
                return False
        return True

