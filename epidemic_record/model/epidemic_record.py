from odoo import api, fields, models


class EpidemicRecord(models.Model):
    """疫情记录"""
    _name = 'epidemic.record'

    name = fields.Char(string='姓名')
    data = fields.Date(string='确诊日期')
    state = fields.Char(string='省份')
    city = fields.Char(string='市区')
    county = fields.Char(string='区/县')
    street = fields.Char(string='详细地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'), ('abroad', '境内')], dafault='within', string='境内/境外')
    is_ill = fields.Boolean(string='是否确诊')
    begin_isolation_date = fields.Date(string='起始隔离日期')
    isolation_mode = fields.Selection([('home', '居家隔离'), ('focus', '集中隔离')], string='隔离方式')
    create_user_id = fields.Many2one('res.users', default=lambda self: self.env.uid, string='提报人')
    note = fields.Text(string='说明')
