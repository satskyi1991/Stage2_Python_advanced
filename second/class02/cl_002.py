

class Shop:
    Name = "Auchan"
    Sales = 0
    def __init__(self, shop_adress, SoldGoods):
        self._shop_adress = shop_adress
        self._SoldGoods = SoldGoods
        Shop.Sales += SoldGoods

    def get_SoldGoods(self):
         return self._SoldGoods

    def set_SoldGoods(self):
        return self._SoldGoods

    def get_shop_adress(self):
         return self._shop_adress

    def set_shop_adress(self):
        return self._shop_adress

    def add_sold(self, quantaty):
        self._SoldGoods += quantaty
        self.Sales      += quantaty

Shop1 = Shop('Shop1', 1000)
Shop2 = Shop('Shop1', 2000)
print (Shop1.get_shop_adress())
print (Shop1.get_SoldGoods())
print (Shop2.get_shop_adress())
print (Shop2.get_SoldGoods())

print(Shop.Sales)