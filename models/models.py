# -*- coding: utf-8 -*-

from odoo import models, fields, api

import eet

class PosConfing(models.Model):
    _inherit = 'pos.config'
    eet_yes = fields.Boolean(string="Is EET requested")
    eet_config_id = fields.Integer(string="EET Config", help='Vazba na id EET config')

