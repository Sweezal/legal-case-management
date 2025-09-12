from odoo import models, fields, api

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'

    name = fields.Char(string='Case Reference', required=True, copy=False, readonly=True, default='New')
    client_id = fields.Many2one('res.partner', string='Client', required=True, domain=[('is_client', '=', True)])
    responsible_lawyer_id = fields.Many2one('res.partner', string='Responsible Lawyer', required=True, domain=[('is_lawyer', '=', True)])
    case_type = fields.Selection([('civil', 'Civil'), ('criminal', 'Criminal'), ('family', 'Family')], string='Case Type')
    stage = fields.Selection([
        ('intake', 'Intake'),
        ('active', 'Active'), 
        ('closed', 'Closed'),
    ], string='Stage', default='intake')
    open_date = fields.Date(string='Open Date', default=fields.Date.context_today)
    close_date = fields.Date(string='Close Date', readonly=True)
    description = fields.Text(string='Case Description')