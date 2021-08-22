class Solution:
   
    def isPalindrome(self, x: int) -> bool:
        y=x
        rev = 0
        while(x > 0):
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
        
        if(rev == y):
            return True
        else:
            return False