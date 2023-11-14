#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0
    print("Item registered")

  def add_item(self, title, price, quantity = 1):
    # self.title = title
    # self.price = price
    # self.quantity = quantity
    self.total += price * quantity
    self.last_transaction = price * quantity
    # (self.items).append(title)
    # return self.items
    
    for i in range(quantity):
      i = 0
      (self.items).append(title)
    # return self.items

  def apply_discount(self):
    percent = self.discount * 0.01
    if ((type(self.discount) == int) and (self.discount > 0)):
      self.total = int(self.total - (self.total * percent))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print(f"There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total -= self.last_transaction


flatiron = CashRegister(discount=10)

flatiron.add_item("cereal", 12, 2)
flatiron.add_item("milk", 2, 3)
print(flatiron.items)