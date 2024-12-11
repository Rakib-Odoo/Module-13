from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    image = fields.Binary(string='Image')

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient,self).default_get(fields)
        res['note'] = 'New Patient Created'
        return res