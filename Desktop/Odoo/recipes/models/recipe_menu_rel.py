from odoo import models,fields,api

class MenuRecipeRel(models.Model):
    _name = 'recipes.menureciperel'
    
    recipe_id = fields.Many2one('recipes.recipe', string='Recipes contained by menu', ondelete='cascade')
    menu_id = fields.Many2one('recipes.menu', string='Menu that contains', ondelete='cascade')
   
    menuRecipeType = fields.Selection([
                                      ('starter', 'Starter'),
                                      ('main', 'Main'),
                                      ('main2', 'Second Main'),
                                      ('dessert', 'Dessert'),
                                      ('sides', 'Sides'),
                                      ('drink', 'Drinks')
                                      ],string ='Type',required=True)
