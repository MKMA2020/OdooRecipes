from odoo import models,fields,api

class User(models.Model):
    _inherit = 'res.users'
    
    userType = fields.Selection([
                           ('normal', 'Normal'),
                           ('premium', 'Premium'),
                           ('admin', 'Admin')
                           ],string = 'Type',required=True)
                           
    ingredients_id = fields.One2many('recipes.ingredient', string='Ingredients created')
    
    menus_id = fields.One2many('recipes.menu', string='Menus created')
    
    recipes_id = fields.One2many('recipes.recipe', string='Recipes created')
    
    userRel_id = fields.One2many('recipes.userreciperel', string='Commenter')