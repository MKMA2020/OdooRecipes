from odoo import models,fields,api

# Model of the user.
class User(models.Model):
    _inherit = 'res.users'
    
    # Type of the user.
    userType = fields.Selection([
                           ('normal', 'Normal'),
                           ('premium', 'Premium'),
                           ('admin', 'Admin')
                           ],string = 'Type',required=True)
    
    # Ingredients created by the user.
    ingredients_id = fields.One2many('recipes.ingredient', 'user_id', string='Ingredients created')
    
    # Menus created by the user.
    menus_id = fields.One2many('recipes.menu', 'user_id', string='Menus created')
    
    # Recipes created by the user.
    recipes_id = fields.One2many('recipes.recipe', 'user_id',  string='Recipes created')
    
    # 
    userRel_id = fields.One2many('recipes.userreciperel', 'user_id',  string='Commenter')