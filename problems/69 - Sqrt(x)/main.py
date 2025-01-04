class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x  # Work directly with the range
        answer = 0  # Initialize to 0, the lowest possible integer square root
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid ** 2 > x:
                right = mid - 1
            else:
                answer = mid  # Update answer with the valid mid
                left = mid + 1
        
        return answer