{
    'name': "Real Estate",
    'summary': "This module has all the great functionality about property",
    'sequence': 5,
    'description': """ Real Estate Module which manage
            - Accounting
            - Construction
            - Raw-materials
            - Clients""",
    'author': "Nikita",
    'depends': ['base'],
    'data': [
                'security/ir.model.access.csv',
                'security/security.xml',
                'views/estate_property_view.xml',
                'views/inherite_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
