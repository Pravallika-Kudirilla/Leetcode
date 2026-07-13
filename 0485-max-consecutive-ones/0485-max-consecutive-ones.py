class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
          max_sum=0
          ans=0
          for i in range(len(nums)): 
            if nums[i]==1:
                ans+=1
                max_sum=max(max_sum,ans)               
            else:                              
                ans=0
          return max_sum
