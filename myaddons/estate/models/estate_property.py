from odoo import fields, models, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(string="名称")
    description = fields.Text(string="描述")
    postcode = fields.Char(string="邮编")
    date_availability = fields.Date(string="可售日期")
    expect_price = fields.Float(string="期望价格")
    selling_price = fields.Float(string="销售价格")
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
