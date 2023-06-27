# Question 2 :Best Time to Buy and Sell Stock
N = int(input())
prices = []
for x in range(N):
    prices.append(int(input()))

minPrice = min(prices[:-1])
index = prices.index(minPrice)
maxPrice =  max(prices[index + 1:])

profit = maxPrice - minPrice if maxPrice > minPrice else 0
print(profit)
