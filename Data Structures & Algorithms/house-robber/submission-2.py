class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # def dp(step, lst):
        #     if step > len(nums):
        #         return max(lst[-1], lst[-2]) if len(lst) > 1 else lst[-1]
        #     if step < 3:
        #         lst.append(nums[step-1])
        #     else:
        #         lst.append(max(lst[step-2] + nums[step-1], lst[step-1]))

        #     return dp(step+1, lst)

        # return dp(1, [0])

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp
        return rob2
