class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lengths=len(nums)
        print(lengths)
        i=0
        count=0
        while i<(lengths-1):
            if(nums[i]==nums[i+1]):
                count=count+1
                if(count==2):
                    nums.remove(nums[i])
                    count=count-1
                    lengths=lengths-1
                else:
                    i=i+1
            else:
                count=0
                i=i+1

        print(nums)
       
        print(len(nums))
        