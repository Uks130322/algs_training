# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


def maxProfit(self, prices: list[int]) -> int:
    result = 0
    begin, end = 0, 0
    for idx in range(len(prices)):
        if prices[begin] > prices[idx]:
            begin = idx
            end = idx
        elif end < len(prices) - 1:
            end += 1
        result = max(result, prices[end] - prices[begin])
    return result


print(maxProfit(0, [7,1,5,3,6,4]))
print(maxProfit(0, [2,1,2,0,0,1]))
print(maxProfit(0, [2,1,4]))
print(maxProfit(0, [1]))

