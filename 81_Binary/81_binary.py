class Solution:
    def search(self, nums, target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True

            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # If nums[l] == nums[m], move left pointer to avoid duplicates
            else:
                l += 1

        return False

sln = Solution()

print(sln.search([2,5,6,0,0,1,2], 3))