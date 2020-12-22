from odoo import models,fields,api

# Recipe model.

class Recipe(models.Model):
    _name = 'recipes.recipe'
        
    name = fields.Char(required=True)
# Types of recipes.
    recipeType = fields.Selection([
                           ('starter', 'Starter'),
                           ('main', 'Main'),
                           ('main2', 'Second Main'),
                           ('dessert', 'Dessert'),
                           ('sides', 'Sides'),
                           ('drink', 'Drinks')
                           ],string = 'Type',required=True)
# Calories of a recipe.
    kCal = fields.Float (required=True)
# Checks if it's veified.    
    verified = fields.Boolean (required=True)
# The ingredients that the recipe is made of.    
    ingredients = fields.Many2many('recipes.ingredient', string='Contains ingredients')
# The id of the user that made the recipe.   
    user_id = fields.Many2one('res.users', string='Recipe owner')
# Comments.
    comments = fields.One2many('recipes.userreciperel', 'user_id', string='Recipe commented')
# The menus where this recipe can be found. 
    menus = fields.One2many('recipes.menureciperel', 'menu_id', string='Recipes contained by menu')
    


