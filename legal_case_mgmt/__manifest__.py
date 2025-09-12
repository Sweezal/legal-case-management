{
    'name': 'Legal Case Management',
    'version': '1.0',
    'summary': 'Manage legal cases, clients, and hearings',
    'category': 'Legal',
    'author': 'Your Name',
    'website': 'http://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',  # ← ADD THIS LINE
        'data/sequence.xml',
        'views/legal_case_views.xml',
        'views/legal_hearing_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}