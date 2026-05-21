class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]] 
        freq = {}
        for st in strs:
            key = "".join(sorted(st))
            if key not in freq:
                freq[key] = [st]
                continue
            freq[key].append(st)
        return list(freq.values())
