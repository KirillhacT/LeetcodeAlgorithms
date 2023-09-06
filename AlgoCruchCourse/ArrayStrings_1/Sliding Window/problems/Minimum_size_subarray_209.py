def minSubArrayLen(self, target, nums):
    left = summ = 0
    ans = float("inf")
    for right in range(len(nums)):
        summ += nums[right]
        while summ >= target:
            ans = min(ans, right - left + 1)
            summ -= nums[left]
            left += 1
        return ans if ans != float("inf") else 0