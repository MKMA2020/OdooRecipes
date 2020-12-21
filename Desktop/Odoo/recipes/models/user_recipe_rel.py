from odoo import models,fields,api

class UserRecipeRel(models.Model):
   _name = 'recipes.userreciperel'
   
   user_id = fields.Many2one('res.users', string='Commenter', ondelete='cascade')
   recipe_id = fields.Many2one('recipes.recipe', string='Recipe commented', ondelete='cascade')
   
   comment = fields.Char(required=True)
   rating = fields.Float(required=True)
