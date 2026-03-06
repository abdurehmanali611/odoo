from odoo import models, fields, api
from datetime import date

class OfficeAsset(models.Model):
    _name = 'office.asset'
    _description = 'Office Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Device Name", required=True)
    serial_number = fields.Char(string="Serial Number")
    price = fields.Float(string="Purchase Price")
    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.company.currency_id)
    age = fields.Integer(string="Asset Age (Days)", compute="_compute_asset_age")

    @api.depends('purchase_date')
    def _compute_asset_age(self):
        for record in self:
            if record.purchase_date:
                delta = date.today() - record.purchase_date
                record.age = delta.days
            else:
                record.age = 0
    
    asset_type = fields.Selection([
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('furniture', 'Furniture'),
        ('other', 'Other')
    ], string="Type", default='laptop')
    assigned_to = fields.Many2one('res.users', string="Assigned User")
    purchase_date = fields.Date(string="Purchase Date")
    state = fields.Selection([
        ('new', 'New'),
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('damaged', 'Damaged')
    ], string="Status", default="new")
    notes = fields.Text(string="Internal Notes")
    image = fields.Binary(string="Asset Image")
    