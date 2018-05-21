# -*- coding: utf-8 -*-
from openerp import models, fields

class citasrgl_cita(models.Model):
    _name= 'citasrgl.cita'
    name= fields.Char(string='Autor de la cita',)
    description= fields.Text(string='Cita')
    date= fields.Datetime(string='Fecha de registro',default=fields.Datetime.now())

