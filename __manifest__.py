# -*- coding: utf-8 -*-
{
    'name': "Project Permission Doyarushka",

    'summary': """
        Access rights and permissions mod for the Project module
        """,

    'author': "Ivan Sova",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'views/project_views.xml',
    ],
}