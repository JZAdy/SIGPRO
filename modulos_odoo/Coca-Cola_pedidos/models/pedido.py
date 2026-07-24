from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CocacolaPedido(models.Model):
    _name = 'cocacola.pedido'
    _description = 'Registro de Pedidos'
    _order = 'fecha_pedido desc'

    cliente = fields.Char(
        string='Cliente',
        required=True,
    )

    producto_id = fields.Many2one(
        'cocacola.productos',
        string='Producto',
        required=True,
    )

    cantidad = fields.Integer(
        string='Cantidad',
        required=True,
        default=1,
    )

    precio_unitario = fields.Float(
        string='Precio unitario',
        related='producto_id.precio',
        store=True,
        readonly=True,
    )

    total = fields.Float(
        string='Total',
        compute='_compute_total',
        store=True,
    )

    fecha_pedido = fields.Date(
        string='Fecha del pedido',
        default=fields.Date.today,
    )

    metodo_pago = fields.Selection([
        ('efectivo_ficticio', 'Efectivo Ficticio'),
        ('tarjeta_ficticia', 'Tarjeta Ficticia'),
        ('transferencia_ficticia', 'Transferencia Ficticia'),
        ('credito_interno_ficticio', 'Crédito Interno Ficticio'),
    ],
        string='Método de pago',
        default='efectivo_ficticio',
        required=True,
    )

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ],
        string='Estado',
        default='borrador',
    )

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total(self):
        for record in self:
            record.total = record.cantidad * record.precio_unitario

    @api.constrains('cantidad')
    def _check_cantidad_positiva(self):
        for record in self:
            if record.cantidad <= 0:
                raise ValidationError('La cantidad del pedido debe ser mayor a cero.')

    def action_confirmar(self):
        for record in self:
            record.estado = 'confirmado'

    def action_entregar(self):
        for record in self:
            record.estado = 'entregado'

    def action_cancelar(self):
        for record in self:
            record.estado = 'cancelado'