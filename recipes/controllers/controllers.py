# -*- coding: utf-8 -*-
from odoo import http

# class Recipes(http.Controller):
#     @http.route('/recipes/recipes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recipes/recipes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recipes.listing', {
#             'root': '/recipes/recipes',
#             'objects': http.request.env['recipes.recipes'].search([]),
#         })

#     @http.route('/recipes/recipes/objects/<model("recipes.recipes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recipes.object', {
#             'object': obj
#         })
