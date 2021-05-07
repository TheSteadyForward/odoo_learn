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
    is_ill = fields.Boolean(string='是否确诊', default=False)
    begin_lsolation_date = fields.Date(string='起始隔离日期')
    lsolation_mode = fields.Selection([('home', '居家隔离'), ('focus', '集中隔离')], string='隔离方式')
    create_user_id = fields.Many2one('res.users', string='当前创建人', default=lambda self: self.env.uid)
    note = fields.Text(string='说明')
    test_float = fields.Float(string='测试浮点数')
    test_int = fields.Integer(string='整型数')

    fuzhu_create_user_ids = fields.Many2many('res.users',
                                             'epidemic_record_res_user_rel',
                                             column1='record_id',
                                             column2='user_id', string='辅助填报人信息')
    active = fields.Boolean(default=True)

    @api.model
    def create(self, value_list):
        """创建方法"""
        res = super(EpidemicRecord, self).create(value_list)
        res.note = "{}省{}市患者，隔离人员姓名{}".format(res.state, res.city, res.name)
        return res
    
    @api.multi
    def write(self, vals):
        """修改方法"""
        res = super(EpidemicRecord, self).write(vals)
        return res

    @api.multi
    def unlink(self):
        """伪删除方法"""

        # 逻辑删除的方法
        for record_obj in self:
            record_obj.active = False
        """
        # 物理删除的方法
        # res = super(EpidemicRecord, self).unlink()
        # return res
        """

    @api.onchange('state', 'city', 'name')
    def onchange_note(self):
        self.note = "{}省{}市患者，隔离人员姓名{}".format(self.state, self.city, self.name)

    @api.multi
    def my_unlink(self):
        self.active = False

    def my_search(self):
        domain = [('is_ill', '=', True)]
        objs = self.search(domain)
        print(objs)

    def create_or_write(self):
        """演示ORM创建或修改"""
        # self.env['res.users'].create({
        #     'name': 'test1',
        #     'email': '1109644698@qq.com',
        #     'login': 'test1'
        # })
        user_obj = self.env['res.users'].search([('name', '=', 'test1')])
        user_obj.write({
            "login": 'test2'
        })
