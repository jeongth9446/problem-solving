class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = collections.defaultdict(int)  # value : index

        start = 0
        res = 0

        for i, item in enumerate(s):
            if item in used and start <= used[item]:
                start = used[item] + 1
                print(start, i - start + 1)
            if i - start + 1 > res:
                res = i - start + 1
            used[item] = i
        return res

