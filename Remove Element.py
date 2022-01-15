class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0

        while i<len(nums):
            if(nums[i]==val):
                nums.remove(val)

                i=i-1
            i=i+1
        print(nums)
        print(len(nums))
        


