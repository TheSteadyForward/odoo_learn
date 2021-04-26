# -*- coding: utf-8 -*-
{
    # 名字
    'name': '疫情记录',
    # 描述
    'summary': """
         疫情记录
    """,
    'description': """
        此模块用来学习Odoo框架，已经进行疫情记录
    """,
    'depends': [],  # 依赖模块
    # 作者
    'author': "YueXiaoMu",
    # 地址
    'website': 'todo',
    # 类别
    'category': '疫情记录',
    # 版本
    'version': '0.1',

    'data': [
        'views/epidemic_record_views.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [],
    'application': True
}