# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class curso(models.Model):
    _name = 'odoo_examen_prueba2.curso'
    _description = 'modelo con los años académicos de distintos cursos'

    ano_curso = fields.Char(string="Ano académico do curso:", size=20, required=True)