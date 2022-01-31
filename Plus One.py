class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val=0
        new=[]
        for i in digits:
            val=val*10+i
        val=val+1
        for j in str(val):
            new.append(j)
        return new
        