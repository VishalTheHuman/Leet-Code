class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount = (100-discount)/100
        self.prod_prices  = {}
        for i in range(len(products)):
            self.prod_prices[products[i]] = prices[i]
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(len(product)):
            total += (self.prod_prices[product[i]]*amount[i])
        self.count+=1
        if self.count%self.n==0:
            return self.discount*total
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
