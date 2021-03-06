from odoo import models,fields,api

#Class of the relation between the user and the recipe, representing commentaries
class UserRecipeRel(models.Model):
    #Developed by Kerman and Martin
    #Name of the model
   _name = 'recipes.userreciperel'
   
   #Many2one field that links with the user. It represents the user that
   #wrote the commentary
   user_id = fields.Many2one('res.users', string='Commenter', ondelete='cascade', default=lambda self: self.env.uid)
   #Many2one field that links with the recipe. It represents the recipe in which
   #the commentary has been written
   recipe_id = fields.Many2one('recipes.recipe', string='Recipe commented', ondelete='cascade', default=lambda self: self.id)
   
   #Char field and required. The text of the commentary
   comment = fields.Char(required=True)
   
   #Float field and required. The rating (from 1 to 5) of the recipe by the user
   rating = fields.Float(required=True)
