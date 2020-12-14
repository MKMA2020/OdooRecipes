from odoo import models

class Menu(models.model):
    __name = 'recipes.menu'
    type = fields.selection([('breakfast','Breakfast'), ('lunch','Confirmed'),('dinner','Dinner'), ('snack','Snack') ], 'Type', default='breakfast')

