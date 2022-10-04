'''
module: electronics.py
    class: Electronics
        attribute: .category
        method: __str__
'''

from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0, category = "Electronics"):
        super().__init__(category, condition)
        self.condition = condition

    def __str__(self): 
        return "A gadget full of buttons and secrets."
