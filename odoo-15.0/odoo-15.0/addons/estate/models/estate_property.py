from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name = "estate.property"
    property_type_id = fields.Many2one('estate.property.type', string='Property Type', required=True)
    x_buyer_id = fields.Many2one('res.partner', string='Buyer')
    x_seller_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    _description = "Real Estate Property"
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date Availability")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True)
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    availability_date = fields.Date('Availability Date', copy=False,default=fields.Date.today() + relativedelta(months=3))
    x_number_of_bedrooms = fields.Integer(string='Number of Bedrooms', default=2)
    x_active = fields.Boolean(string='Active', default=True)
    x_state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', default='new', required=True, copy=False)
    garden_orientation = fields.Selection([
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West')
    ], string="Garden Orientation")

    @api.model
    def create(self, values):
        if 'selling_price' in values:
            raise ValidationError('You cannot set the selling price manually.')
        return super(EstateProperty, self).create(values)
