from odoo import models,fields,api
import re

class Recipe(models.Model):
    #Developed by Martin Gros and Martin Valiente
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
    
    user_id = fields.Many2one('res.users', string='Recipe owner', default = lambda self: self.env.uid)
    
    comments = fields.One2many('recipes.userreciperel', 'user_id', string='Recipe commented')
    
    menus = fields.One2many('recipes.menureciperel', 'menu_id', string='Recipes contained by menu')

    @api.constrains('name')   
    def _check_name(self):
        for recipe in self:
            if not re.match("^[a-zA-Z]+$", recipe.name):
                raise ValidationError("Please enter valid name.")


