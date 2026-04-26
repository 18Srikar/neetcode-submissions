class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # 'first' represents n-2, 'second' represents n-1
        first, second = 1, 2
        
        for i in range(3, n + 1):
            # Calculate the current step
            current = first + second
            # Shift the window forward
            first = second
            second = current
            
        return second
