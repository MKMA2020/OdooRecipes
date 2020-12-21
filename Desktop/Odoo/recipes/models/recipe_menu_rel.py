from odoo import api
from odoo import fields
from odoo import models

class MenuRecipeRel(models.Model):
    #Relationship class between menu and recipe.
    _name = 'recipes.menureciperel'
    
    #recipe_id field for the MenuRecipeRel model. Will contain the relation with
    #the Recipe id that contains the menus.
    recipe_id = fields.Many2one('recipes.recipe',
                                string='Recipes contained by menu',
                                ondelete='cascade')
    
    #menu_id field for the MenuRecipeRel model. Will contain the relation with 
    #the Menu id that contains the recipes.
    menu_id = fields.Many2one('recipes.menu',
                              string='Menu that contains',
                              ondelete='cascade')
   
    menuRecipeType = fields.Selection([
                                      ('starter', 'Starter'),
                                      ('main', 'Main'),
                                      ('main2', 'Second Main'),
                                      ('dessert', 'Dessert'),
                                      ('sides', 'Sides'),
                                      ('drink', 'Drinks')
                                      ], string='Type', required=True)
                                      