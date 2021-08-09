# -*- coding: utf-8 -*-
{
    'name': "pfe_topnet",
    'summary': """
    'author': 'GHARBI Rima',
        Gestion des dossiers clients TOPNET""",

    'description': """
       
      """,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'GHARBI Rima',
    'website': 'www.topnet.tn',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/client.xml',
        'views/user.xml',
        'views/templates.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence':'0',
    'images': ['static/description/banner.png']
}
