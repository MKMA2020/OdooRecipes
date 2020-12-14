from odoo import models, fields

class Ingredient(models.model):
    __name = 'recipes.ingredient'
    
    id = fields.Integer(requiered=True),
    name = fields.char(requered=True),
    type = fields.selection([('dairy','Dairy'), ('fatNoil','Fat and Oil'), ('additive','Additive'),('mushroom','Mushroom'), ('legume','Legume'), ('vegetable','Vegetable'), ('fruit','Fruit'), ('egg','Egg'), ('cereal','Cereal'),('fish','Fish'), ('seafood','Seafood'), ('meat','Meat'), ('drink','Drink'), ('dessert','Dessert') ],'Tipo')
    
    