# -*- coding: utf-8 -*-
# from odoo import http


# class OdooExamenPrueba2(http.Controller):
#     @http.route('/odoo_examen_prueba2/odoo_examen_prueba2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_examen_prueba2/odoo_examen_prueba2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_examen_prueba2.listing', {
#             'root': '/odoo_examen_prueba2/odoo_examen_prueba2',
#             'objects': http.request.env['odoo_examen_prueba2.odoo_examen_prueba2'].search([]),
#         })

#     @http.route('/odoo_examen_prueba2/odoo_examen_prueba2/objects/<model("odoo_examen_prueba2.odoo_examen_prueba2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_examen_prueba2.object', {
#             'object': obj
#         })

