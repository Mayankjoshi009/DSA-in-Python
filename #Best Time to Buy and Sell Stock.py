#Best Time to Buy and Sell Stock 

prices = [7,1,5,3,6,4,8,9,2,10]

n = len(prices)
max_profit = 0
for i in range(n):
    for j in range(i+1, n):
        if prices[j] > prices[i]:
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

print("Maximum profit:", max_profit) 

#TC: O(n^2)
#SC: O(1)

#Optimized Solution
print("Optimized Solution:")

max_profit = 0
min_price = float('inf')
n = len(prices)
for i in range(n):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price)

print("Maximum profit:", max_profit)

#TC: O(n)
#SC: O(1)
           