from odoo import models, fields

class Recipe(models.Model):
    __name = 'recipes.recipe'
        
    name = fields.Char(required=True)
    
    ingredient = fields.Char(required=True)
    
    recipeType = fields.Selection([
                           ('starter', 'Starter'),
                           ('main', 'Main'),
                           ('main2', 'Second Main'),
                           ('dessert', 'Dessert'),
                           ('sides', 'Sides'),
                           ('drink', 'Drinks')
                           ], 'Type')
    
    kCal = fields.Float (required=True)
    
    verified = fields.Boolean (required=True)
    
    ingredients = fields.Many2many('recipes.ingredient', string='Contains ingredients')
    
    user_id = fields.Many2one('res.user', string='Recipe owner')
    
    Comments = fields.One2many('recipes.UserRecipeRel', string='Recipe commented')
    
    Menus = fields.One2many('recipes.MenuRecipeRel', string='Recipes contained by menu')


