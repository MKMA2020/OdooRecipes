from odoo import models, fields

class Menu(models.Model):
    __name = 'recipes.menu'
       
    name = fields.Char(required=True)
    
    menuType = fields.Selection([
                           ('breakfast','Breakfast'),
                           ('lunch','Lunch'),
                           ('snack','Snack'),
                           ('dinner','Dinner')
                           ],'Tipo')(required=True)
    
    user_id = fields.Many2one('res.users', string='Menu owner')
    
    menuRel_id = fields.One2many('res.MenuRecipeRel', string='Menu has recipes')