from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CocaColaProductos(models.Model):
    _name = 'cocacola.productos'
    _description = 'Productos Coca-Cola'
    _order = 'name'

    name = fields.Char(
        string='Nombre del producto',
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
        string='Categoría del producto',
        required=True,
        default='otro',
    )

    linea_id = fields.Many2one(
        'cocacola.linea',
        string='Línea de producto',
        domain="[('categoria', '=', categoria)]",
        required=True,
    )

    tamano = fields.Selection([
        ('350ml', '350ml'),
        ('600ml', '600ml'),
        ('1l', '1 Litro'),
        ('2l', '2 Litros'),
        ('otro', 'Otro'),
    ],
        string='Tamaño',
        default='350ml',
    )

    precio = fields.Float(
        string='Precio del producto',
        required=True,
        default=0.0,
    )

    stock = fields.Integer(
        string='Stock del producto',
        required=True,
        default=0,
    )

    fecha_ingreso = fields.Date(
        string='Fecha de ingreso',
        default=fields.Date.today,
    )

    fecha_vencimiento = fields.Date(
        string='Fecha de vencimiento',
    )

    imagen = fields.Binary(
        string='Imagen del producto',
    )

    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('agotado', 'Agotado'),
    ],
        string='Estado',
        default='activo',
    )

    @api.constrains('precio', 'stock')
    def _check_valores_positivos(self):
        for record in self:
            if record.precio < 0:
                raise ValidationError('El precio no puede ser negativo.')
            if record.stock < 0:
                raise ValidationError('El stock no puede ser negativo.')

    @api.onchange('categoria')
    def _onchange_categoria(self):
        self.linea_id = False