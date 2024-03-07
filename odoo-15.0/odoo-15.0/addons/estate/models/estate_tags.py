from odoo import api, fields, models
class EstatePropertyTags(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tags'
    name = fields.Char(string='Name', required=True)
