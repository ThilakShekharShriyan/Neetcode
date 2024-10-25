
# 121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/



prices = [7,6,4,3,1]


l , r ,n = 0,0, len(prices)-1

mP = 0


while l < n:

    p = prices[r] - prices[l]
    mP = max(mP , p)

    if p < 0 or r == n:
        l+=1
        r = l
    r+=1

print(mP)
    




