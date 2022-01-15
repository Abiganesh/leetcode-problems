class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lengths=len(nums)
        i=0

        while i<(lengths-1):
            if(nums[i]==nums[i+1]):
                nums.remove(nums[i])
                lengths=lengths-1
                i=i-1

            i=i+1
        print(nums)
        print(len(nums))

       