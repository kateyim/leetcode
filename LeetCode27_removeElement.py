"""
LeetCode 27 移除元素
一 题目描述
给你一个数组 nums 和一个值 val 
你需要 原地 移除所有数值等于 val的元素 并返回移除后数组的新长度
不要使用额外的数组空间Y你必须仅使用 O(1) 额外空间并 原地修改输入数组
元素的顺序可以改变 
你不需要考虑数组中超出新长度后面的元素
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


re = Solution()
nums1 = [3, 2, 2, 3]
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(re.removeElement(nums1, 3))  # 输出：2
print(re.removeElement(nums2, 2))  # 输出：5    