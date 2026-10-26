class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for c in strs[0]:
            out += c
        
        for i in range(1, len(strs)):
            k = 0
            s = strs[i]
            while k < len(out) and k < len(s) and s[k] == out[k]:
                k += 1
            if k == 0:
                out = ""
                break
            out = out[:k]

        return out