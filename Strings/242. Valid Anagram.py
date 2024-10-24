def isAnagram(self, s: str, t: str):

    #Solution 1: using collections.Counter
    # return sorted(s) == sorted(t)


    # Solution 2: using dictionary and list
    # if len(s) != len(t):
    # return False
    
    # s_d = defaultdict(int)
    # t_d = defaultdict(int)

    # for i in range(len(s)):
    #     s_d[s[i]]+=1
    #     t_d[t[i]]+=1
    
    # return s_d == t_d
    return 0