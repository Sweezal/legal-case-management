{
    'name': "Legal Case Management",
    'version': '1.0',
    'depends': ['base', 'mail', 'account'],
    'author': "Your Team Name",
    'category': 'Legal',
    'description': "A minimal app to manage legal cases, clients, lawyers, and hearings.",
    'data': [
        'security/ir.model.access.csv',  # Basic access
        'views/menus.xml',               # Main menu
        'views/legal_case_views.xml',    # Case screens
        'views/legal_hearing_views.xml', # Hearing screens
        'views/res_partner_views.xml',   # Partner views
    ],
    'demo': ['data/demo_data.xml'],
    'application': True,
}