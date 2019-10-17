# -*- coding: utf-8 -*-
from odoo import http

# class EetPosModule(http.Controller):
#     @http.route('/eet_pos_module/eet_pos_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eet_pos_module/eet_pos_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eet_pos_module.listing', {
#             'root': '/eet_pos_module/eet_pos_module',
#             'objects': http.request.env['eet_pos_module.eet_pos_module'].search([]),
#         })

#     @http.route('/eet_pos_module/eet_pos_module/objects/<model("eet_pos_module.eet_pos_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eet_pos_module.object', {
#             'object': obj
#         })