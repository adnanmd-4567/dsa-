from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq, key = lambda x:freq[x], reverse=True)
        result = ""
        for char in sorted_chars:
            result += char * freq[char]
        return result