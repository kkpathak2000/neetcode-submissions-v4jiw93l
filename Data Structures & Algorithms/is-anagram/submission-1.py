class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if ch in freq:
                if freq[ch]==0:
                    freq[ch]=freq.get(ch,0)+1
                else:
                    freq[ch]=freq.get(ch,0)-1
        return sum(freq.values()) == 0

            