# -*- coding: utf-8 -*-
from odoo import http

# class Citasrgl(http.Controller):
#     @http.route('/citasrgl/citasrgl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasrgl/citasrgl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasrgl.listing', {
#             'root': '/citasrgl/citasrgl',
#             'objects': http.request.env['citasrgl.citasrgl'].search([]),
#         })

#     @http.route('/citasrgl/citasrgl/objects/<model("citasrgl.citasrgl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasrgl.object', {
#             'object': obj
#         })