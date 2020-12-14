from odoo import models, fields

class User(models.model):
    __name = 'recipes.ingredient'
    
    id = fields.Long(required=True)
    login = fields.char(required=True)
    email = fields.char(required=True)
    fullName = fields.char(required=True)
    status = field.bool(required=True)
    password = fields.char(required=True)
    lastAccess = field.datetime(required=True)
    lastPasswordChange = field.datetime(required=True)
    type = field.selection([('normal',Normal),('premium',Premium),('admin',Admin)])