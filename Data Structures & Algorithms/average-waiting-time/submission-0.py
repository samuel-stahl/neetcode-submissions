class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ends = []
        wait_sum = 0
        n = len(customers)

        for i in range(n):
            arrival = customers[i][0]
            start = arrival if not ends else max(ends[-1], arrival)
            end = start + customers[i][1]
            ends.append(end)
            wait = end - arrival
            wait_sum += wait

        return wait_sum / n