from odoo import models

class Menu(models.model):
    __name = 'recipes.menu'
    
    id = fields.Integer(requiered=True),
    name = fields.char(requered=True),
    type = fields.selection([('breakfast','Breakfast'), ('lunch','Lunch'), ('snack','Snack'), ('dinner','Dinner')],'Tipo'),

