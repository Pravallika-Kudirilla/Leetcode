class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket=defaultdict(int)
        count=0
        left=0
        for right in range(len(fruits)):
            basket[fruits[right]]+=1
            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1
            count=max(count,right-left+1)
        return count