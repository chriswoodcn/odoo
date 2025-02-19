from odoo import fields, models, api
from datetime import timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(string="名称", required=True)
    description = fields.Text(string="描述")
    postcode = fields.Char(string="邮编")
    date_availability = fields.Date(
        string="可售日期",
        copy=False,
        default=lambda self: fields.Datetime.now() + timedelta(month=3),
    )
    expect_price = fields.Float(string="期望价格", required=True)
    selling_price = fields.Float(string="销售价格", readonly=True, copy=False)
    bedrooms = fields.Integer(string="卧室数量")
    living_area = fields.Integer(string="使用面积")
    facades = fields.Integer(string="面")
    garage = fields.Boolean(string="是否含车库")
    garden = fields.Boolean(string="是否含花园")
    garden_area = fields.Integer(string="花园面积")
    garden_orientation = fields.Selection(
        string="花园朝向",
        selection=[("north", "北"), ("south", "南"), ("east", "东"), ("west", "西")],
    )
    active=fields.Boolean(string="是否归档", default=True)
    state = fields.Selection(
        string="状态",
        selection=[("new", "新"), ("offer_received", "收到报价"), ("offer_accepted", "接受报价"), ("sold", "售出"), ("canceled", "取消")],
        copy=False,
        default="new",
    )
