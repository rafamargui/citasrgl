# -*- coding: utf-8 -*-
{
    'name': "citasrgl",

    'summary': """
        Aplicacion creada para el curso DAM""",

    'description': """
        Citas
    """,

    'author': "Rafael Gonzalez de la Llera",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/citasrgl_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}