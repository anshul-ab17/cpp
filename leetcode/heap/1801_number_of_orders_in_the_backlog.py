# Use max heap for buys and min heap for sells.
import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10 ** 9 + 7
        buy, sell = [], []

        for price, amount, order_type in orders:
            if order_type == 0:
                heapq.heappush(buy, (-price, amount))
            else:
                heapq.heappush(sell, (price, amount))

            while buy and sell and -buy[0][0] >= sell[0][0]:
                b_price, b_amount = heapq.heappop(buy)
                s_price, s_amount = heapq.heappop(sell)
                traded = min(b_amount, s_amount)
                b_amount -= traded
                s_amount -= traded
                if b_amount > 0:
                    heapq.heappush(buy, (b_price, b_amount))
                if s_amount > 0:
                    heapq.heappush(sell, (s_price, s_amount))

        total = sum(a for _, a in buy) + sum(a for _, a in sell)
        return total % MOD
