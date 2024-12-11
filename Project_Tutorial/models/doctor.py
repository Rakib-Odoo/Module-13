from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender')
    note = fields.Text(string='Description')
    image = fields.Binary(string='Image')

    @api.model
    def default_get(self, fields_list):
        res = super(HospitalDoctor, self).default_get(fields_list)
        res['note'] = 'New Doctor Created'
        return res