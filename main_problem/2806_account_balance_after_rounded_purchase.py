import math


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - round(purchaseAmount / 10) * 10 if purchaseAmount % 10 != 5 else 100 - math.ceil(purchaseAmount / 10) * 10
