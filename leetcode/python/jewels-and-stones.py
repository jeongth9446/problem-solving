class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()

        for item in stones:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        res = 0
        for item in jewels:
            if item not in stones:
                continue
            if item in jewels:
                res += d[item]

        return res
