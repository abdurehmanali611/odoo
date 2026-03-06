{
    'name': 'Office Asset Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Track office hardware and furniture',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_views.xml'
    ],
    'installable': True,
    'application': True
}