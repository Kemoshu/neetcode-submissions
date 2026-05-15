class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dct:
                dct[key] = []
            dct[key].append(i)
        return list(dct.values())