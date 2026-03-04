from odoo import models, fields

class OfficeAsset(models.Model):
    _name = 'office.asset'
    _description = 'Office Asset'
    name = fields.Char(string="Device Name", required=True)
    serial_number = fields.Char(string="Serial Number")
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
    