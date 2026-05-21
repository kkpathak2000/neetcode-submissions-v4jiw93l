class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]] 
        freq = {}
        for st in strs:
            if "".join(sorted(st)) not in freq:
                freq["".join(sorted(st))] = [st]
            else:
                freq["".join(sorted(st))].append(st)
        return list(freq.values())
