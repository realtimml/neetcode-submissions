from string import ascii_lowercase
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ascii_lowercase.index(c)] += 1
            key = tuple(key)

            groups[key].append(s)
        
        return list(groups.values())