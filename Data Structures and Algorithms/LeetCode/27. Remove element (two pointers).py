# left and right

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        while (left <= right):
            if nums[left] == val:
                if nums[right] == val:
                    right -= 1
                else:
                    nums[left] = nums[right]
                    nums[right] = val
                    left += 1
            else:
                left += 1
        return left

# fast and slow

# public int removeElement(int[] nums, int val) {
#     int i = 0;
#     for (int j = 0; j < nums.length; j++) {
#         if (nums[j] != val) {
#             nums[i] = nums[j];
#             i++;
#         }
#     }
#     return i;
# }

# left and right

# public int removeElement(int[] nums, int val) {
#     int i = 0;
#     int n = nums.length;
#     while (i < n) {
#         if (nums[i] == val) {
#             nums[i] = nums[n - 1];
#             // reduce array size by one
#             n--;
#         } else {
#             i++;
#         }
#     }
#     return n;
# }
