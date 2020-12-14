from odoo import models

class Recipe(models.model):
    __name = 'recipes.recipe'
    id = fields.Integer(requiered=True)
    name = fields.Char(requiered=True)
    ingredient = fields.Char(requiered=True)
    type = fields.selection([('starter','Starter'), ('main','Main'), ('main2','Second Main'),('dessert','Dessert'), ('sides','Sides'), ('drink','Drinks') ],'Type', default='breakfast')
    
    kCal = fields.float (requiered = True)
    verified = fields.Boolean (requiered = True)


