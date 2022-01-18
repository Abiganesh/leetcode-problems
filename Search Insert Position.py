class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif(max(nums)<target):
            return len(nums)

        else:
            for i in nums:
                if(i>target):
                    closest_value=i
                    print(closest_value)
                    return nums.index(closest_value)
