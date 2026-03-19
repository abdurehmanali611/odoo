from odoo import models, fields, api
from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # ================= ASSIGNMENT =================
    assigned_person_id = fields.Many2one(
        'res.users',
        string="Assigned Person"
    )

    # ================= PROCESS STAGE FIELDS =================
    source_details = fields.Text(string="Source Details")
    client_requirements = fields.Text(string="Client Requirements")
    notes = fields.Text(string="Notes")

    # ================= APPROVAL =================
    approval_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending', string="Approval Status")

    # ================= BUTTON ACTIONS =================
    def action_assign(self):
        if not self.env.user.has_group('crm_lead_workflow_custom.group_department_manager'):
            raise UserError("Only managers can assign.")
        return True

    def action_approve(self):
        if not self.env.user.has_group('crm_lead_workflow_custom.group_department_manager'):
            raise UserError("Only managers can approve.")
        self.approval_status = 'approved'

    def action_reject(self):
        if not self.env.user.has_group('crm_lead_workflow_custom.group_department_manager'):
            raise UserError("Only managers can reject.")
        self.approval_status = 'rejected'

    # ================= STAGE VALIDATION =================
    def write(self, vals):
        if 'stage_id' in vals:
            new_stage = self.env['crm.stage'].browse(vals['stage_id'])

            for lead in self:
                # Rule 1: Cannot go to Process without assignment
                if new_stage.name == 'Process' and not lead.assigned_person_id:
                    raise UserError("You must assign a person before moving to Process stage.")

                # Rule 2: Cannot go to Approval without required data
                if new_stage.name == 'Approval' and not lead.client_requirements:
                    raise UserError("Fill client requirements before moving to Approval.")

        return super().write(vals)