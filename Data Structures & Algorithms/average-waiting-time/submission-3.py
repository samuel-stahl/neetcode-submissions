class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        end = 0
        wait_sum = 0
        n = len(customers)

        for i in range(n):
            arrival = customers[i][0]
            start = max(end, arrival)
            end = start + customers[i][1]
            wait_sum += (end - arrival)

        return wait_sum / n