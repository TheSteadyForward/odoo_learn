from odoo import api, fields, models


class EpidemicRecord(models.Model):
    """疫情记录表"""
    _name = 'epidemic.record'
    _description = '疫情记录表'

    name = fields.Char(string='姓名')
    date = fields.Date(string='确诊日期')  # xxx年xx月xx日
    state = fields.Char(string='省份')
    city = fields.Char(string='市')
    county = fields.Char(string='区/县')
    street = fields.Char(string='详细地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'), ('abroad', '境外')], default='within', string='境内/境外感染')
    is_ill = fields.Boolean(string='是否确诊')
    begin_lsolation_date = fields.Date(string='起始隔离日期')
    lsolation_mode = fields.Selection([('home', '居家隔离'), ('focus', '集中隔离')], string='隔离方式')
    create_user_id = fields.Many2one('res.users', string='当前创建人', default=lambda self: self.env.uid)
    note = fields.Text(string='说明')
