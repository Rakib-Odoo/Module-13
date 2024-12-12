from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Name', required=True, tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True, tracking=True)
    note = fields.Text(string='Description', default='New Appointment Created')
    date_appointment = fields.Date(string="Appointment Date", default=fields.Date.context_today, required=True, tracking=True)
    date_checkup = fields.Datetime(string="Check Up Time", required=True, default=fields.Datetime.now, tracking=True)
    prescription = fields.Text(string="Prescription")

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status")

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    sl = fields.Char(string='SL NO', required=True, copy=False, readonly=True, index=True,
                     default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl', _('New')) == _('New'):
            vals['sl'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.model
    def default_get(self, fields):
        res = super(HospitalAppointment, self).default_get(fields)
        if 'prescription' in fields:  # Ensure the 'prescription' field exists in the fields list
            res['prescription'] = 'New Prescription Created'
        return res
