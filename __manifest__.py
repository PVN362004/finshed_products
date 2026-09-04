{
    'name': 'Finished Products',
    'version': '19.0.1.0.0',
    'category': 'Management',
    'summary': 'Finished Products',
    'author': 'Nhan',
    'license': 'AGPL-3',
    'depends': ['base', 'product', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/finished_product_views.xml',
        'reports/report.xml',
        'reports/product_tags_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -1,
}