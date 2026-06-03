# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class ciclo(models.Model):
    _name = 'odoo_examen_prueba2.ciclo'
    _description = 'modelo con con los distintos tipos de ciclos'
    _sql_constraints = [('ciclo_unico', 'unique(ciclo)', 'Non se pode repetir o ciclo')]
    _rec_name = 'ciclo'

    ciclo = fields.Char(string="Ciclo:", size=20, required=True)