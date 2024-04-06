class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price
    
    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print('Init MixinLog')
        self.ID += 1
        self.id = self.ID
    
    def save_sell_log(self):
        print(f'{self.id}: товар був проданий в 00:00 годин')
    
    def print_info(self):
        print('Виводиться з класу MixinLog')


class NoteBook(Goods, MixinLog):
    pass
    # def print_info(self):
    #     MixinLog.print_info(self)


n = NoteBook('Acer', 1.5, 30000)
n.save_sell_log()
print(NoteBook.__mro__, end='\n\n')

n.print_info()
MixinLog.print_info(n)