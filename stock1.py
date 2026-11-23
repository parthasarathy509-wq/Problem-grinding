def maxProfit(prices: list[int]) -> int:
    left = 0  # Buy day
    max_profit = 0

    for right in range(1, len(prices)):  # Sell day
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            # Found a lower price; shift buy pointer here
            left = right

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4, 0, 2]))  # Expected: 5 (Late crash after max profit)
print(maxProfit([3, 8, 2, 5, 1, 7]))  # Expected: 6 (Multiple minimum resets)
print(maxProfit([9, 9, 7, 5, 5, 2, 1]))  # Expected: 0 (Strictly non-increasing + dupes)
print(maxProfit([5]))  # Expected: 0 (Single element edge case)
print(maxProfit([2, 10, 2, 11]))  # Expected: 9 (Duplicate minimum floor mid-way)
print(
    maxProfit([10000, 0, 10000, 0, 9999])
)  # Expected: 10000 (Max constraint volatility)
