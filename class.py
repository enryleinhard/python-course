class Flower:

  def __init__(self, name, petals, price):
    self.name = name
    self.petals = petals
    self.price = price

  def info(self):
    print(f'{self.name}, {self.petals}, {self.price}')

  def edit_name(self, new_name):
    self.name = new_name

  def edit_petals(self, new_petals):
    self.petals = new_petals

  def edit_price(self, new_price):
    self.price = new_price

  def get_name(self):
    return self.name

  def get_petals(self):
    return self.petals
  
  def get_price(self):
    return self.price

a = input('Name: ')
b = int(input('Petals: '))
c = float(input('Price: '))

flower = Flower(a, b, c)
flower.info()

print('--------Edit each type-------------')

newname = input('Name: ')
flower.edit_name(newname)

newpetals = int(input('Petals: '))
flower.edit_petals(newpetals)

newprice = float(input('Price: '))
flower.edit_price(newprice)

print('---------Retrieve each type---------')

name = flower.get_name()
petals = flower.get_petals()
price = flower.get_price()

print(name)
print(petals)
print(price)