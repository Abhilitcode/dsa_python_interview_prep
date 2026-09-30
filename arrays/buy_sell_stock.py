# Approach 2 o(n), O(1)
# always buy cheaper and sell maximum 
# Keep the cheapest price seen so far, calculate today's profit using it, and keep the maximum profit.

def buy_n_sell(stocks):
    minimum_prcie = stocks[0]
    max_profit = 0

    for i in range(1,len(stocks)):
        #todays profit
        profit = stocks[i] - minimum_prcie

        max_profit = max(max_profit,profit)

        #cheapest price seen so far
        minimum_prcie = min(minimum_prcie, stocks[i])

    return max_profit

stocks = list(map(int,input("enter an array: ").split())) 
obj = buy_n_sell(stocks)
print(obj)







#Appraoch 1 : O(n^2)
#[7 1 5 3 6 4]

# def buy_n_sell(stocks):
#     profit = 0
#     max_profit = 0
#     for i in range(len(stocks)):
#         for j in range(i+1, len(stocks)):
#             profit = stocks[j] - stocks[i]
#             max_profit = max(max_profit,profit)

#     return max_profit

# stocks = list(map(int,input("enter an array: ").split())) 
# obj = buy_n_sell(stocks)
# print(obj)