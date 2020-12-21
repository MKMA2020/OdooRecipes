from odoo import models,fields,api

# Model of the relation between user and recipe.
class UserRecipeRel(models.Model):
   _name = 'recipes.userreciperel'
   
   user_id = fields.Many2one('res.users', string='Commenter', ondelete='cascade')
   recipe_id = fields.Many2one('recipes.recipe', string='Recipe commented', ondelete='cascade')
   
   # Text of a comment on a recipe.
   comment = fields.Char(required=True)
   # Rating given by a comment on a recipe.
   rating = fields.Float(required=True)
