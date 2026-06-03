# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class curso(models.Model):
    _name = 'odoo_examen_prueba2.curso'
    _description = 'modelo con los años académicos de distintos cursos'
    _sql_constraints = [('ano_unico', 'unique(ano_curso)', 'Non se pode repetir o ano académico')]
    _rec_name = 'ano_curso'

    ano_curso = fields.Char(string="Ano académico do curso:", size=20, required=True)