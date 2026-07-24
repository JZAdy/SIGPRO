{
    'name': 'Registro de Empleados',
    'version': '1.0',
    'summary': 'Módulo para el registro y consulta de empleados',
    'description': 'Permite registrar empleados con nombre, apellido, edad, ocupación y años trabajados.',
    'author': 'Andy Morales',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/empleado_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}