class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = list()
        out.append(1)
        p = 1
        for i in range(0, len(nums) - 1):
            p *= nums[i]
            out.append(p)

        p = 1
        for i in range(len(nums) - 1, 0, -1):
            p *= nums[i]
            out[i - 1] *= p

        return out