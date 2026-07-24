{
    'name': 'Registro de Pedidos',
    'version': '1.0',
    'summary': 'Módulo para el registro y seguimiento de pedidos',
    'description': 'Permite registrar pedidos asociados a productos del catálogo Coca-Cola, con cálculo automático de total y método de pago ficticio.',
    'author': 'Andy Morales',
    'category': 'Sales',
    'depends': ['base', 'Coca-Cola'],
    'data': [
        'security/ir.model.access.csv',
        'views/pedido_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}