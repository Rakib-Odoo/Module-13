from odoo import api, fields, models, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender', tracking=True)
    note = fields.Text(string='Description')
    image = fields.Binary(string='Image')

    @api.model
    def default_get(self, fields_list):
        res = super(HospitalDoctor, self).default_get(fields_list)
        res['note'] = 'New Doctor Created'
        return res

    sl = fields.Char(string='SL NO', required=True, copy=False, readonly=True, index=True,
                     default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sl',_('New')) == _('New'):
            vals['sl'] = self.env['ir.sequence'].next_by_code('hospital.doctor') or _('New')
        res = super(HospitalDoctor, self).create(vals)
        return res