from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    product_ids = fields.One2many(
        'product.template', 'user_id', string="Productos"
    )
