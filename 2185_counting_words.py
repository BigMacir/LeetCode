class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        matches = 0
        for word in words:
            if word.find(pref) == 0:
                matches += 1
        return matches