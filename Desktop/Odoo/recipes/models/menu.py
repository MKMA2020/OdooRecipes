from odoo import models

class Menu(models.model):
    __name = 'recipes.menu'
   
    id = fields.Integer(required=True),
    name = fields.char(required=True),
    type = fields.selection([('breakfast','Breakfast'), ('lunch','Lunch'), ('snack','Snack'), ('dinner','Dinner')],'Tipo')