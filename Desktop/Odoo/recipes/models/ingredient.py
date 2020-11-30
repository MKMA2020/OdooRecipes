from odoo import models, fields

class Ingredient(models.model):
    __name = 'recipes.ingredient'
    
    id = fields.Integer(requiered=True),
    name = fields.char(requered=True),
    
    type = fields.selection((('n','Unconfirmed'), ('c','Confirmed')),'Tipo'),
    
    