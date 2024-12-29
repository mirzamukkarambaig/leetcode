# Solution 1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for digit in digits:
            number = number * 10 + digit
        number += 1

        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10

        digits.reverse()

        return digits

# Solution 2
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
    
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits 
            else:
                digits[i] = 0  
        
        return [1] + digits