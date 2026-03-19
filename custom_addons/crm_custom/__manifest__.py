{
    'name': 'CRM Lead Workflow Custom',
    'summary': 'Custom CRM Workflow with Assignment and Approval',
    'version': '1.0',
    'depends': ['crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/stages.xml',
        'views/crm_views.xml',
    ],
    'installable': True,
    'application': True,
    'author': 'Abdu Alta'
}