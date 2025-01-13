# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/


def maxProfit(self, prices: list[int], fee: int) -> int:
    without = 0
    with_stock = -(prices[0])
    for price in prices[1:]:
        without = max(without, price + with_stock - fee)
        with_stock = max(with_stock, without - price)

    return without


print(maxProfit(0, [1,3,2,8,4,9], 2))
print(maxProfit(0, [1,3,7,5,10,3], 3))