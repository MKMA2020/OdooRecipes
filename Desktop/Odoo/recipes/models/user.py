from odoo import models, fields

class User(models.Model):
    __inherit = 'res.users'
    
    userType = fields.Selection([
                           ('normal','Normal'),
                           ('premium','Premium'),
                           ('admin','Admin')
                           ])(required=True)
                           
    ingredients_id = fields.One2many('recipes.ingredient', string='Ingredients created')
    
    menus_id = fields.One2many('recipes.menu', string='Menus created')
    
    recipes_id = fields.One2many('recipes.recipe', string='Recipes created')
    
    UserRel_id = fields.One2many('res.UserRecipeRel', string='Commenter')