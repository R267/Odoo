{
    'name': "Real Estate Advertisement",
    'summary': "A module for managing real estate advertisements",
    'description': "This module allows users to manage real estate advertisements within Odoo.",
    'author': "Chernyshov Roman",
    'category': """Estate Advertisement Management""",
    'version': '1.0.0',
    'depends': ['base'],
    'sequence':-100,
    'data': [
         'security/ir.model.access.csv',
         'security/security.xml',
         'views/estate_property_views.xml',
         'views/estate_data.xml',
         'views/estate_menus.xml',
         'views/estate_property_search_views.xml',
         'views/estate_property_type_form.xml',
         'views/estate_property_type_tree.xml',
         'views/estate.property.offer.xml',

    ],
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
    'auto_install': False,
    'website':'www.estate_advertisment.com',

}
