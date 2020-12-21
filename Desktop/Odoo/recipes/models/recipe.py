from odoo import models,fields,api

class Recipe(models.Model):
    _name = 'recipes.recipe'
        
    name = fields.Char(required=True)
    
    recipeType = fields.Selection([
                           ('starter', 'Starter'),
                           ('main', 'Main'),
                           ('main2', 'Second Main'),
                           ('dessert', 'Dessert'),
                           ('sides', 'Sides'),
                           ('drink', 'Drinks')
                           ],string = 'Type',required=True)
    
    kCal = fields.Float (required=True)
    
    verified = fields.Boolean (required=True)
    
    ingredients = fields.Many2many('recipes.ingredient', string='Contains ingredients')
    
    user_id = fields.Many2one('res.users', string='Recipe owner')
    
    comments = fields.One2many('recipes.userreciperel', string='Recipe commented')
    
    menus = fields.One2many('recipes.menureciperel', string='Recipes contained by menu')
    


