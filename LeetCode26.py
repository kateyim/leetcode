from typing import List
"""
LeetCode 26：删除有序数组中的重复项。

题目描述

给你一个 升序排列 的数组 nums，请你 原地 删除重复出现的元素，使每个元素只出现一次，并返回删除后数组的新长度 k。

元素的相对顺序应该保持一致。

由于不能真正改变数组长度，你需要把去重后的结果放在 nums 的前 k 个位置中。也就是说，函数返回 k 后，nums[:k] 应该是去重后的数组。

要求：

原地修改 nums
只能使用 O(1) 额外空间
返回去重后的长度 k
不需要关心 nums[k:] 后面的内容
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们只需要遍历一次数组。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储指针 i 和 j。

rd = Solution()
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(rd.removeDuplicates(nums1))  # 输出：2
print(rd.removeDuplicates(nums2))  # 输出：5
