class Solution(object):
    def containsDuplicate(self, nums):
        unsorted = len(nums)
        distinct_nums = len(set(nums))
        return distinct_nums < unsorted 
        