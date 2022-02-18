from odoo import models, fields
from datetime import datetime, timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    def x(self):
        initial_date = datetime.now()
        date_after_three_months = initial_date + timedelta(days=90)
        return date_after_three_months
    
    name = fields.Char(string="Name", required=True)
    buyer = fields.Many2one("res.partner", string="Buyer", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    seller = fields.Many2one("res.users", string="Salesperson")
    date_availability = fields.Date(copy=False, string="Available From", default=x)
    expected_price = fields.Float(required=True, string="Expected Price")
    selling_price = fields.Float(string="Selling Price", readonly=True)
    bedrooms = fields.Integer(default=2, string="Bedrooms")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
    )
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new'
    )

