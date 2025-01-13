# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


def maxProfit(self, prices: list[int]) -> int:
    result = 0
    local_sum = 0
    begin, end = 0, 0
    while begin < len(prices) - 1:
        if prices[begin] >= prices[begin + 1]:
            begin += 1
            end = max(end, begin)
            continue
        if end < len(prices) - 1 and prices[end] <= prices[end + 1]:
            end += 1
            local_sum = prices[end] - prices[begin]
        else:
            result += local_sum
            begin = end
    return result


print(maxProfit(0, [7,1,5,3,6,4]))
print(maxProfit(0, [7,1,5,3,6,8]))
print(maxProfit(0, [1,2,3,4,5]))
print(maxProfit(0, [7,6,4,3,1]))