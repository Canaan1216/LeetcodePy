# -*- coding:utf-8 -*-
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例：
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = { }
        for i, num in enumerate(nums):
        #"enumerate()" can change a list to a index array
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i

if __name__ == '__main__':
    # do test
    testDemo = Solution()
    print testDemo.twoSum([2, 7, 11, 15],9)