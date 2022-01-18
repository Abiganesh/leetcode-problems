class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            absolute_difference_function = lambda list_value : abs(list_value - target)
            closest_value = min(nums, key=absolute_difference_function)
            if(closest_value>target):
                val=nums.index(closest_value)-1
                if(val<0):
                    return 0
                elif(val==0):
                    return 1
            else:
                return nums.index(closest_value)+1