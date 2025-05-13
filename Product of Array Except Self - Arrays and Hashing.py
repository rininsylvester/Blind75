class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            final[i] = pre
            pre = pre * nums[i]
        suf = 1
        for i in range(len(nums) -1 , -1 , -1):
            final[i] = final[i] * suf
            suf = suf * nums[i]
        return final        
