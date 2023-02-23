LeetCode 217 Easy 

Solution I used

```from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            if n in d:
                return True
            d[n]+=1
        return False  
```

Instead of Iterating through the whole loop return True for the first duplicate appearance ( I Like Using Dictionaries You can use a Set as well)


    