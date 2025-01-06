class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def f(n):
            if n in memo:
                return memo[n]
            
            memo[n] = f(n - 1) + f(n - 2)
            return memo[n]
        return f(n)
        