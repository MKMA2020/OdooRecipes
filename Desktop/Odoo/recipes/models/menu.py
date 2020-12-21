from odoo import models,fields,api

class Menu(models.Model):
    _name = 'recipes.menu'
       
    name = fields.Char(required=True)
    
    menuType = fields.Selection([
                           ('breakfast','Breakfast'),
                           ('lunch','Lunch'),
                           ('snack','Snack'),
                           ('dinner','Dinner')
                           ],string = 'Tipo', required=True)
    
    user_id = fields.Many2one('res.users', string='Menu owner')
    
    menuRel_id = fields.One2many('recipes.menureciperel', string='Menu has recipes')