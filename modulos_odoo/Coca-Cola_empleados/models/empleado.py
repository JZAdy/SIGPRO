import hashlib
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CocacolaEmpleado(models.Model):
    _name = 'cocacola.empleado'
    _description = 'Registro de Empleados'
    _order = 'apellido, nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True,
    )

    apellido = fields.Char(
        string='Apellido',
        required=True,
    )

    edad = fields.Integer(
        string='Edad',
        required=True,
    )

    ocupacion = fields.Selection([
        ('vendedor', 'Vendedor'),
        ('produccion', 'Producción'),
        ('gerencia', 'Gerencia'),
        ('logistica', 'Logística'),
        ('atencion_cliente', 'Atención al Cliente'),
        ('otro', 'Otro'),
    ],
        string='Ocupación',
        required=True,
        default='otro',
    )

    anios_trabajados = fields.Integer(
        string='Años trabajados',
        default=0,
    )

    nombre_completo = fields.Char(
        string='Nombre completo',
        compute='_compute_nombre_completo',
        store=True,
    )

    # ---- Acceso al portal web (antes vivía en el módulo aparte) ----
    usuario = fields.Char(string='Usuario de acceso')
    clave_hash = fields.Char(string='Clave (hash)')

    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellido}"

    @api.constrains('edad', 'anios_trabajados')
    def _check_valores_positivos(self):
        for record in self:
            if record.edad < 18:
                raise ValidationError('La edad debe ser mayor o igual a 18 años.')
            if record.anios_trabajados < 0:
                raise ValidationError('Los años trabajados no pueden ser negativos.')
            if record.anios_trabajados > (record.edad - 16):
                raise ValidationError('Los años trabajados no son coherentes con la edad registrada.')

    def set_clave(self, clave_plana):
        """Guarda la clave como hash, nunca en texto plano."""
        self.clave_hash = hashlib.sha256(clave_plana.encode('utf-8')).hexdigest()

    @api.model
    def verificar_credenciales(self, usuario, clave_plana):
        empleado = self.search([('usuario', '=', usuario)], limit=1)
        if not empleado:
            return False
        clave_hash = hashlib.sha256(clave_plana.encode('utf-8')).hexdigest()
        if empleado.clave_hash == clave_hash:
            return {
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellido': empleado.apellido,
                'ocupacion': empleado.ocupacion,
            }
        return False