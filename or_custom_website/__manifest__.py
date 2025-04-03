# -*- coding: utf-8 -*-
{
    'name': "Custom Website Oscar Romero",
    'summary': "Personalización del sitio web en Odoo",
    'description': "Extensión para usuarios que permite asociar productos a cada usuario.",
    'author': "Luis Millan",
    'category': 'Website',
    'version': '0.1',
    'depends': ['base', 'website', 'website_sale'],
    'data': [
        'views/res_users_views.xml', 
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
