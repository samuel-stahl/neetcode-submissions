class Solution:
    def climbStairs(self, n: int) -> int:

        # if n == 1 or n == 2:
        #     return n
        
        # def dp(step, lst):
        #     if step > n:
        #         return lst[-1]

        #     lst.append(lst[step - 1] + lst[step - 2])

        #     return dp(step + 1, lst)

        # return dp(3, [0, 1, 2])

        one_prev, two_prev = 1, 1

        for _ in range(n-1):
            temp = one_prev
            one_prev = one_prev + two_prev
            two_prev = temp

        return one_prev