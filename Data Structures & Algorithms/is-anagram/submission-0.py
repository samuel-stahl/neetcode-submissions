class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        if len(s) != len(t):
            return False

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        
        for c in t:
            if c not in s_dict:
                return False
            s_dict[c] = s_dict[c] - 1
            if s_dict[c] == 0:
                s_dict.pop(c)

        return not s_dict