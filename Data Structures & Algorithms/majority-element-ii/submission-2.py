class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3
        dic = {}
        res = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if (not res or num not in res) and dic[num] > target:
                res.append(num)

        return res