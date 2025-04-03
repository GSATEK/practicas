from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    user_id = fields.Many2one('res.users', string="Usuario")
