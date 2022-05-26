from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_b = strs.copy()
        str_c = []
        str_d = dict()
        cnt = 0
        res = []
        for item in str_b:
            if ("".join(sorted(item)) in str_d):
                str_c.append(str_d["".join(sorted(item))])
            else:
                str_d["".join(sorted(item))] = cnt
                str_c.append(str_d["".join(sorted(item))])
                res.append([])
                cnt = cnt + 1

        for i in range(0, len(strs)):
            res[str_c[i]].append(str_b[i])

        return res