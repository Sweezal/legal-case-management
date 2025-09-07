{
    'name': "Legal Case Management",
    'version': '1.0',
    'depends': ['base', 'mail', 'account'],
    'author': "Your Team Name",
    'category': 'Legal',
    'description': "A minimal app to manage legal cases, clients, lawyers, and hearings.",
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'application': True,
}