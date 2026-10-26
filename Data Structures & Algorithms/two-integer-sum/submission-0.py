class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in dic:
                dic[num] = i
            check = target - num
            if check in dic:
                if dic[check] != i:
                    return [dic[check], i]

        return []

