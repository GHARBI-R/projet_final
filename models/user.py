#-*- coding: utf-8 -*-

from odoo import models, fields, api


class TopnetUser(models.Model):
     _name = 'topnet.user'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'users topnet'


     name = fields.Char(string='Nom', required=True)

     gender = fields.Selection(
        [
            ('Homme', 'Homme'),
            ('femme', 'Femme'),
        ], default='Homme', string='Sexe', required=True
     )
     cin = fields.Integer(string='cin', required=True)
     email = fields.Char(string='Email', required=True)
     password = fields.Char(string='Mot de passe', required=True)
     role = fields.Selection(
        [
            ('Administrateur', 'Administrateur'),
            ('ChefZone', 'Chef de Zone'),
            ('ChefAgence', 'Chef Agence'),
            ('Agent', 'Agent'),

        ],
        required=True,
        default='Agent'
     )

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
