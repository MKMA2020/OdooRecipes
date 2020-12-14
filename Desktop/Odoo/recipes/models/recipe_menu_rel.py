from odoo import fields
from odoo import models

class MenuRecipeRel(models.Model):
    
    recipe_id = fields.Many2one('recipes.recipe', string='Recipes contained by menu', ondelete='cascade')
    menu_id = fields.Many2one('res.menu', string='Menu that contains', ondelete='cascade')
   
    menuRecipeType = fields.Selection([
                                      ('starter', 'Starter'),
                                      ('main', 'Main'),
                                      ('main2', 'Second Main'),
                                      ('dessert', 'Dessert'),
                                      ('sides', 'Sides'),
                                      ('drink', 'Drinks')
                                      ],'Type')(required=True)
