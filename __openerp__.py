# -*- coding: utf-8 -*-
{
    'name': "Upload CSV",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Teckzilla",
    'website': "http://www.teckzilla.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account' ],
    'price': 199.99,
    'currency': 'EUR',

    # always loaded
    'data': [

        'wizard/upload_csv.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}