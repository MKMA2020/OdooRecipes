from odoo import models,fields,api

class Ingredient(models.Model):
    _name = 'recipes.ingredient'
        
    name = fields.Char(required=True)
    
    ingredientType = fields.Selection([
                           ('dairy','Dairy'),
                           ('fatNoil','Fat and Oil'),
                           ('additive','Additive'),
                           ('mushroom','Mushroom'),
                           ('legume','Legume'),
                           ('vegetable','Vegetable'),
                           ('fruit','Fruit'),
                           ('egg','Egg'),
                           ('cereal','Cereal'),
                           ('fish','Fish'),
                           ('seafood','Seafood'),   
                           ('meat','Meat'),
                           ('drink','Drink'),
                           ('dessert','Dessert')
                           ],string='Type',required=True)
    
    user_id = fields.Many2one('res.users', string='Ingredient creator')
    
    menus = fields.Many2many('recipes.menu', string='Part of menus')
    
    recipes = fields.Many2many('recipes.recipe', string='Part of recipes')