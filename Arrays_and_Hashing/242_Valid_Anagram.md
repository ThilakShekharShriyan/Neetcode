Leetcode 242 Easy

Solution I Used

```
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = defaultdict(int)
        if len(s)!=len(t):
            return False

        for i in s:
            d[i]+=1
        
        for i in t:
            if d[i]==0:
                return False
            d[i]-=1
        return True
```


Check if the length of strings are not equal. 

Use a Dictionary to count the number of occurences in s and incremented by 1. Run another for loop and decrement it by 1 . if it reaches -1 return False.
