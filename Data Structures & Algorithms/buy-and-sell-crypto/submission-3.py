class Solution:
    def maxProfit(self, prices: List[int]) -> int:      
        p=0
        buy=prices[0]
        for each in prices:
            p=max(p,each-buy)
            buy=min(buy,each)
        return p
            
                
        