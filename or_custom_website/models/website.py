# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import SUPERUSER_ID, _, _lt, api, fields, models, tools
from odoo.http import request
from odoo.osv import expression

from odoo.addons.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = 'website'

    def _get_checkout_step_list(self):
        self.ensure_one()
        is_extra_step_active = self.viewref('website_sale.extra_info').active
        redirect_to_sign_in = self.account_on_checkout == 'mandatory' and self.is_public_user()

        steps = [(['website_sale.cart'], {
            'name': _lt("Revisar Solicitud"),
            'current_href': '/shop/cart',
            'main_button': _lt("Registrate") if redirect_to_sign_in else _lt("Verificar"),
            'main_button_href': f'{"/web/login?redirect=" if redirect_to_sign_in else ""}/shop/checkout?express=1',
            'back_button':  _lt("Volver a la tienda"),
            'back_button_href': '/shop',
        }), (['website_sale.checkout', 'website_sale.address'], {
            'name': _lt("Información"),
            'current_href': '/shop/checkout',
            'main_button': _lt("Confirmar"),
            'main_button_href': f'{"/shop/extra_info" if is_extra_step_active else "/shop/confirm_order"}',
            'back_button':  _lt("Volver al Articulo"),
            'back_button_href': '/shop/cart',
        })]
        if is_extra_step_active:
            steps.append((['website_sale.extra_info'], {
                'name': _lt("Extra Info"),
                'current_href': '/shop/extra_info',
                'main_button': _lt("Continue checkout"),
                'main_button_href': '/shop/confirm_order',
                'back_button':  _lt("Return to shipping"),
                'back_button_href': '/shop/checkout',
            }))
        steps.append((['website_sale.payment'], {
            'name': _lt("Solicitar"),
            'current_href': '/shop/payment',
            'back_button':  _lt("Volver al Articulo"),
            'back_button_href': '/shop/cart',
        }))
        return steps