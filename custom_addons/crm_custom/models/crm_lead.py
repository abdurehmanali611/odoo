from odoo import models, fields

class Customer(models.Model):
    _name = "custom.customer"
    _description = "Customer"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone", required=True)
    phone2 = fields.Char(string="Second Phone", required=False)
    email = fields.Char(string="Email", required=False)
    region = fields.Selection(
        [
            ("Addis Ababa", "Addis Ababa"),
            ("Dire Dawa", "Dire Dawa"),
            ("Oromia", "Oromia"),
            ("Amhara", "Amhara"),
            ("Southern nation nationality and people", "Southern nation nationality and people"),
            ("Gambela", "Gambela"),
            ("Tigray", "Tigray"),
            ("Afar", "Afar"),
            ("Benishangul-Gumuz", "Benishangul-Gumuz"),
            ("Central Ethiopia", "Central Ethiopia"),
            ("Harari", "Harari"),
            ("Sidama", "Sidama"),
            ("Somali", "Somali"),
            ("South-western Ethiopia", "South-western Ethiopia"),
        ],
        string="Region",
        required=True,
    )
    city = fields.Char(string="City", required=True)
    company = fields.Char(string="Company Name", required=False)
    Lead_Source = fields.Selection(
        [
            ("Walk-in", "Walk-in"),
            ("Social Media", "Social Media"),
            ("Phone", "Phone"),
            ("Referral", "Referral")
        ], string="Lead Source", required=True
    )
    interest=fields.Selection([
        ("End-to-End IT Infrastructure Solutions", "End-to-End IT Infrastructure Solutions"),
        ("Software Licensing & Enterprise Applications", "Software Licensing & Enterprise Applications"),
        ("Banking Automation", "Banking Automation"),
        ("Client Hardware", "Client Hardware"),
        ("Office Automation & Document Management", "Office Automation & Document Management"),
        ("Smart Collaboration Technologies", "Smart Collaboration Technologies"),
        ("Custom Software Development & Integration", "Custom Software Development & Integration"),
        ("Consulting, Training and Technical Support Services", "Consulting, Training and Technical Support Services")
    ], string="Interested Service/Product", required=True)
    follow_up_Date = fields.Date(string="Follow Up Date", required=True)
    description = fields.Text(string="Description", required=False)
    status = fields.Selection([
        ("new", "New"),
        ("Contacted", "Contacted"),
        ("Qualified", "Qualified"),
        ("Proposal", "Proposal"),
        ("Won", "Won"),
        ("Lost", "Lost")
    ], default="new")

    def action_set_contacted(self):
        self.status = "Contacted"

    def action_set_qualified(self):
        self.status = "Qualified"

    def action_set_proposal(self):
        self.status = "Proposal"

    def action_set_won(self):
        self.status = "Won"

    def action_set_lost(self):
        self.status = "Lost"



