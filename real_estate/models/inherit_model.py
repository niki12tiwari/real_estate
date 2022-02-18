from odoo import models, fields


class InheritProperty(models.Model):
    _inherit = "res.users"

    line = fields.One2many("estate.property", "seller", string="Real Estate Property")
