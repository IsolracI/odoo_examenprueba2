# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class modulo(models.Model):
    _name = 'odoo_examen_prueba2.modulo'
    _description = 'modelo con con los distintos tipos de modulos'
    _sql_constraints = [('modulo_unico', 'unique(name)', 'Non se pode repetir o modulo')]

    name = fields.Char(string="Modulo", size=20, required=True)
    descripcion = fields.Text(string="Descripción")