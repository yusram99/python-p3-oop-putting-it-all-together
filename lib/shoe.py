#!/usr/bin/env python3

# class Shoe:
#     def __init__(self, brand, size, price):
#         self.brand = brand
#         self.size = size
#         self.price = price

#     def __str__(self):
#         return f"{self.brand} shoe, size {self.size}, price{self.price}"

#     def is_affordable(self):
#         return self.price <= 100
class Shoe:
    def __init__(self, brand, size, price):
        self.brand = brand
        self._size = size
        self.price = price
        self._condition = "New"
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("The shoe has been repaired.")
        self._condition = "New"
