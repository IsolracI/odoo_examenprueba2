# -*- coding: utf-8 -*-
from odoo import models, fields, api
import os

class nota(models.Model):
    _name = 'odoo_examen_prueba2.nota'
    _description = 'modelo con con las notas de los alumnos'

    ano_academico = fields.Many2one("odoo_examen_prueba2.curso", string="Ano académico")
        #fields.Char(string="Ano Académico", size=20, required=True))
    ciclo = fields.Many2one("odoo_examen_prueba2.ciclo", string="Ciclo")
        #fields.Text(string="Ciclo"))
    quenda = fields.Selection([('ordinario','Ordinario'),('vespertino','Vespertino'),('fpdual','FPDual')], string="Quenda")
    curso = fields.Selection([('1ero','1º'),('2do','2º')], string="Curso")
    modulo = fields.Many2one("odoo_examen_prueba2.modulo", string="Módulo")
        #fields.Char(string="Módulo")) #RELACION
    nota = fields.Integer(string="Nota")
    nota_texto = fields.Char(compute="_calcular_nota_texto", string="Nota Texto")

    @api.depends('nota')
    def _calcular_nota_texto(self):
        for registro in self:
            if registro.nota < 5:
                registro.nota_texto = 'Suspenso'
            elif registro.nota == 5:
                registro.nota_texto = 'Aprobado'
            elif registro.nota == 6:
                registro.nota_texto = 'Bén'
            elif registro.nota >= 7 and registro.nota < 9:
                registro.nota_texto = 'Notable'
            elif registro.nota >= 9:
                registro.nota_texto = 'Sobresaínte'