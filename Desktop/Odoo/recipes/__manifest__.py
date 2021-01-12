# -*- coding: utf-8 -*-
{
    'name': "Recipes",

    'summary': """
        This module will allow the creation, management and view of recipes.""",

    'description': """
        The module will have a recipe creation view, a recipem search view,
        a recipe modification view and a recipe view.
        Recipes can also be deleted or modified.
    """,

    'author': "Pocket Chef",
    'website': "http://www.pocketchef.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/recipeViews.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}