
from odoo import models, fields, api


class PriorityLines(models.Model):
    _name = 'project_sla.priority_lines'

    from_date = fields.Date()
    to_date = fields.Date()
    count = fields.Integer()
    unit = fields.Char()


class PriceLines(models.Model):
    _name = 'project_sla.price_lines'

    from_date = fields.Date()
    to_date = fields.Date()
    price = fields.Float()
    currency = fields.Reference('res.currency', 'symbol')
    # price = fields.Many2one('project_sla.price')


class Price(models.Model):
    _name = 'project_sla.price'

    name = fields.Char()
    code = fields.Integer()
    price_lines = fields.One2many('project_sla.price_lines', 'id')


class Priority(models.Model):
    _name = 'project_sla.priority'

    name = fields.Char()
    code = fields.Integer()
    priority_lines = fields.One2many('project_sla.priority_lines', 'id')


class Project_sla(models.Model):
    _name = 'project_sla.project_sla'

    name = fields.Char()
    performer_price =   fields.Reference([('project_sla.priority',)])
    customer_price =  fields.Reference([('project_sla.price',)])
    performer_price = fields.Reference([('project_sla.price',)])
    customer_priority = fields.Reference([('project_sla.priority',)])

class Project(models.Model):
    _inherit = ['project.task']
    project_sla = fields.Reference([('project_sla.project_sla',)])

