
# 121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

prices = [1,2]


l , r , n = 0 ,0, len(prices)

mP = 0

while l < n and r < n:

    pr = prices[r] - prices[l]
    print(l , r , pr ,mP, prices)
    if pr < 0:
        l+=1
        r=l
        continue
    mP = max(pr , mP)
    r+=1
    if r == n:
        l+=1
        r = l
    

print(mP)

