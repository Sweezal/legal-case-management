{
    'name': "Legal Case Management",
    'version': '1.0',
    'depends': ['base', 'mail', 'account'],
    'author': "Your Team Name",
    'category': 'Legal',
    'description': "A minimal app to manage legal cases, clients, lawyers, and hearings.",
    'data': [
<<<<<<< HEAD
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/case_report.xml',  # <-- ADD THIS LINE
        'views/legal_case_views.xml',
        'views/legal_hearing_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
=======
        'security/ir.model.access.csv',  # Basic access
        'views/menus.xml',               # Main menu
        'views/legal_case_views.xml',    # Case screens
        'views/legal_hearing_views.xml', # Hearing screens
        'views/res_partner_views.xml',   # Partner views
>>>>>>> ade470b8037bc475e3987936ded1730e653422c0
    ],
    'demo': ['data/demo_data.xml'],
    'application': True,
}