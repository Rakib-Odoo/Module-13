from odoo import api, models, fields, _


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
    sl = fields.Char(string='SL NO', required=True, copy=False, readonly=True, index=True,
                     default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl', _('New')) == _('New'):
            vals['sl'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient,self).create(vals)
        return res

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['note'] = 'New Patient Created'
        return res
