# -*- coding: utf-8 -*-

from odoo import models, fields, api
from gdata.sites.data import Field

class TestingModel(models.Model):
    _name       = 'testing.model'
    # defining the fields
    tel         =   fields.Char(string="Phone",         required=True)
    first_name  =   fields.Char(string="First Name",    required=True)  
    last_name   =   fields.Char(string="Last Name",     required=True)
    address     =   fields.Text(string="Address")
    town        =   fields.Char(string="Town",          required=True)
    zip         =   fields.Char(string="Zip",           required=True)
    maile       =   fields.Char(string="Email",         required=True)

     

# class testing(models.Model):
#     _name = 'testing.testing'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100