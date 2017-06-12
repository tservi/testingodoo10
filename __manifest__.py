# -*- coding: utf-8 -*-
# more info here : http://www.odoo.com/documentation/10.0/reference/module.html#reference-module-manifest
{
    'name': "testing",

    'summary': """
        Testing Odoo 10 modules creation
        """,

    'description': """
        No other purpose to test the Odoo 10 modules creation
    """,

    'author': "Jean Tinguely Awais",
    'website': "http://www.t-servi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Testing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}


