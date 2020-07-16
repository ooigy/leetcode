# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # dp array contains len of LIS that ends at pos i
#         # for every i in [0, len(nums)), i = max(j in dp[0: i-1] where
#         # num[j] < num[i])
#         if not nums: return 0
#         dp = [1] * len(nums)
#         for i in range(0, len(nums)):
#             for j in range(0, i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], 1+ dp[j])
#         return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         # attempin to improve above sol
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(0, len(nums)):
            dp[i] = max(1, max((dp[j] for j in range(i) if nums[j] < nums[i]), default=0) + 1)
        return max(dp)

# Above from approx 2100 ms -> 1000 ms