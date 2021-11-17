class Solution(object):
    def divide( dividend, divisor):
        MAX = 2147483647
        MIN = -2147483648
       
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX
        
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        # Quotient
        quotient = 0
        
        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)
       
        while absoluteDividend >= absoluteDivisor:
           
            shift = 0
            while absoluteDividend >= (absoluteDivisor << shift):
                shift += 1
            
            quotient += (1 << (shift - 1))
            
            absoluteDividend -= absoluteDivisor << (shift - 1)
        return -quotient if sign == -1 else quotient
    a = 10
    b = 3
    print(divide(a, b))
    a = 43
    b = -8
    print(divide(a, b))