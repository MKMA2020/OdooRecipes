from odoo import api
from odoo import fields
from odoo import models

#Model of the menu
class Menu(models.Model):
    
    #Name of the model in the database
    _name = 'recipes.menu'
    
    #Name of the menu. Char type and required
    name = fields.Char(required=True)
    
    description = fields.Char(required=True)

    
    #Type of the menu, can be one of these. Selection type, and is required
    menuType = fields.Selection([
                                ('breakfast', 'Breakfast'),
                                ('lunch', 'Lunch'),
                                ('snack', 'Snack'),
                                ('dinner', 'Dinner')
                                ], string='Type', required=True)
    
    #Links this model with users, represents the creator of the menu. Many2one with users
    user_id = fields.Many2one('res.users', string='Menu owner', default=lambda self: self.env.uid)
    
    #Links the menu to the recipes, represents the recipes inside of the menu. One2many with Menu_recipe_rel
    menurel_id = fields.One2many('recipes.menureciperel', 'recipe_id', string='Menu has recipes')
