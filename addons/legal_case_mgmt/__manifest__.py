{
    'name': "Legal Case Management",
    'version': '1.0',
    'depends': ['base', 'mail', 'account'],
    'author': "Your Team Name",
    'category': 'Legal',
    'description': "A minimal app to manage legal cases, clients, lawyers, and hearings.",
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/case_report.xml',  # <-- ADD THIS LINE
        'views/legal_case_views.xml',
        'views/legal_hearing_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'application': True,
}