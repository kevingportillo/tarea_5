class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Fondos Insuficientes.")
#cambios

        elif(len(self.items_list())<=0):
            print("Carrito vacío")
        else:
            self.owner.wallet.withdraw(self.total_amount())
            print("compra realizada")
            seller = self.items[0].owner
            seller.wallet.deposit(self.total_amount())

            for item in self.items_list():
                item.set_owner(self.owner)
        print("Se han entregado los productos")
        self.items.clear()

#cambios
        #else:
            #for item in self.items:
                #item.owner.wallet.balance += item.price  
                #self.owner.wallet.balance -= item.price
                #item.owner = self.owner  
            #self.items = []