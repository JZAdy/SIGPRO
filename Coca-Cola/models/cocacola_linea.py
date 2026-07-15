from odoo import fields, models


class CocaColaLinea(models.Model):
    _name = 'cocacola.linea'
    _description = 'Línea de producto Coca-Cola'
    _order = 'categoria, name'

    name = fields.Char(
        string='Nombre de la línea',
        required=True,
    )

    categoria = fields.Selection([
        ('gaseosa', 'Gaseosa'),
        ('agua', 'Agua'),
        ('jugo', 'Jugo'),
        ('bebida_deportiva', 'Bebida Deportiva'),
        ('te_cafe', 'Té/Café'),
        ('otro', 'Otro'),
    ],
        string='Categoría',
        required=True,
    )

    active = fields.Boolean(
        string='Activo',
        default=True,
    )