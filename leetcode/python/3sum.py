from typing import List


class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:

                sum = nums[i] + nums[left] + nums[right]
                print(sum)
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:  # sum == 0
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


print(Solution.threeSum([-1, 0, 1, 2, -1, -4]))
