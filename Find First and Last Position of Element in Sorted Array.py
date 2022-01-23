class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=None
        maxs=0
        if target in nums:
            val=nums.count(target)
            if(val==1):
                return([nums.index(target),nums.index(target)])
            for j in range(0,len(nums)):
                if(nums[j]==target):
                    if(low==None):
                        low=j
                    else:
                        if(maxs<j):
                            maxs=j

            return ([low,maxs])
        else:
            return ([-1,-1])

        