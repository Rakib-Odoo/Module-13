from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment Information'

    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Appointment Date", default=fields.Date.context_today, required=True)
    date_checkup = fields.Datetime(string="Check Up Time", required=True)
    prescription = fields.Text(string="Prescription")

    @api.model
    def default_get(self, fields_list):
        res = super(HospitalAppointment, self).default_get(fields_list)
        res['note'] = 'New Appointment Created'
        return res