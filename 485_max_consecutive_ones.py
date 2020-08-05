# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # idea: maintain two counter; one local and one global
        # if == 1, increase local counter
        # if != 1, take max(local, global), reset local
        # O(n) run time, O(1) space

        local_counter, global_counter = 0, 0
        for i in nums:
            if i == 1:
                local_counter += 1
            else:
                global_counter = max(local_counter, global_counter)
                local_counter = 0
        return max(local_counter, global_counter)