


#https://leetcode.com/problems/daily-temperatures/description/


temperatures = [30,40,50,60]


#BRutre Force
# res = []
# n = len(temperatures)
# i = 0
# while i < n:

   
#     print(i)
#     j = i+1
#     ctr = 1
#     while j < n:
        
#         if temperatures[j] > temperatures[i]:
#             break
#         print(j , end = "")
#         j+=1
#         ctr+=1
#     ctr = 0 if j == n else ctr
#     res.append(ctr)
#     i+=1
# print(res)


#USing Stack

res = [] #( val , ind)

