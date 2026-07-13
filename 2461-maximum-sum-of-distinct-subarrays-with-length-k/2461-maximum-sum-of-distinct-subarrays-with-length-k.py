class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        window_sum=0
        ans=0
        for i in range(k):
            window_sum+=nums[i]
            freq[nums[i]]+=1
        if len(freq)==k:
            ans=window_sum
        for i in range(k,len(nums)):
            left=nums[i-k]
            window_sum-=left
            freq[left]-=1
            if freq[left]==0:
                del freq[left]
            right=nums[i]
            window_sum+=right
            freq[right]+=1

            if len(freq)==k:
                ans=max(window_sum,ans)
        return ans