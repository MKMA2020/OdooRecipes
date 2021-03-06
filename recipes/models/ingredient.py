from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
import re

class Ingredient(models.Model):
    # Developed by Martin Valiente Ainz
    #Odoo model name identification
    _name = 'recipes.ingredient'
    
    #Name field for the Ingredient model. Char and required type.
    name = fields.Char(required=True, string='Name')
    
    #IngredientType field for the Ingredient model. Selection and required type.
    ingredientType = fields.Selection([
                                      ('dairy', 'Dairy'),
                                      ('fatNoil', 'Fat and Oil'),
                                      ('additive', 'Additive'),
                                      ('mushroom', 'Mushroom'),
                                      ('legume', 'Legume'),
                                      ('vegetable', 'Vegetable'),
                                      ('fruit', 'Fruit'),
                                      ('egg', 'Egg'),
                                      ('cereal', 'Cereal'),
                                      ('fish', 'Fish'),
                                      ('seafood', 'Seafood'), 
                                      ('meat', 'Meat'),
                                      ('drink', 'Drink'),
                                      ('dessert', 'Dessert')
                                      ], string='Type', required=True)
    
    #user_id field for the Ingredient model. Will contain the relation with the 
    #user that created the ingredient.
    user_id = fields.Many2one('res.users', string='Ingredient creator', default=lambda self: self.env.uid)
    
    #recipes field for the Ingredient model. Will contain the relation with the 
    #recipes that contain the ingredients.
    recipes = fields.Many2many('recipes.recipe', string='Part of recipes')
            
    @api.constrains('name')   
    def _check_name(self):
        for ingredient in self:
            if not re.match("^[a-zA-Z]+$", ingredient.name):
                raise ValidationError("Please enter valid name.")
