# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class ciclo(models.Model):
    _name = 'odoo_examen_prueba2.ciclo'
    _description = 'modelo con con los distintos tipos de ciclos'
#    _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o Nome')]

    ciclo = fields.Char(string="Ciclo:", size=20, required=True)