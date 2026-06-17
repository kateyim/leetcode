from typing import List
"""LeetCode 485：最大连续1的个数。
""题目描述
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
示例 1：
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2：
输入：nums = [1,0,1,1,0,1]
输出：2
解释：第二个和第三个 1 之间的连续 1 的个数是 2.

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        for num in nums:
            if num == 1:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                current_consecutive = 0
        
        return max_consecutive 
    
re = Solution()
nums1 = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]
nums3 = [0, 0, 0, 0]
nums4 = [1, 1, 1, 1]
print(re.findMaxConsecutiveOnes(nums1))  # 输出：3  
print(re.findMaxConsecutiveOnes(nums2))  # 输出：2
print(re.findMaxConsecutiveOnes(nums3))  # 输出：0
print(re.findMaxConsecutiveOnes(nums4))  # 输出：4
# 时间复杂度：O(n)，其中 n 是数组 nums 的长度。我们需要遍历一次数组来计算最大连续 1 的个数。
# 空间复杂度：O(1)，我们只使用了常数级别的额外空间来存储 max_consecutive 和 current_consecutive 变量。