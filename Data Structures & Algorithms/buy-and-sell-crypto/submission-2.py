class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_dq = deque()
        max_dq = deque()
        
        start = 0 
        max_profit = 0
        
        best_buy = -1
        best_sell = -1
        for end in range(len(prices)):
            
            while min_dq and prices[min_dq[-1]] > prices[end]:
                min_dq.pop()
            min_dq.append(end)
            
            while max_dq and prices[max_dq[-1]] < prices[end]:
                max_dq.pop()
            max_dq.append(end)
            
            while min_dq[0] > max_dq[0]:
                if start == min_dq[0]:
                    min_dq.popleft()
                if start == max_dq[0]:
                    max_dq.popleft()
                
                start += 1
            
            profit = prices[max_dq[0]] - prices[min_dq[0]]
            if profit > max_profit:
                max_profit = profit
                best_buy = min_dq[0]
                best_sell = max_dq[0]
        return max_profit
        