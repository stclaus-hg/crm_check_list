from openerp import models, fields


class Stage(models.Model):
    _inherit = 'crm.case.stage'

    check_list_id = fields.One2many('crm.lead.check.list.item', 'stage_id')


class Lead(models.Model):
    _inherit = 'crm.lead'

    check_list_id = fields.One2many('crm.lead.check.list.value', 'lead_id')


class CheckListItem(models.Model):
    _name = "crm.lead.check.list.item"

    stage_id = fields.Many2one('crm.case.stage', string="Stage")
    name = fields.Char('Name', required=True)
    is_required = fields.Boolean('Mandatory?')
    order = fields.Integer('Sort Order', default=0)


class CheckListValue(models.Model):
    _name = "crm.lead.check.list.value"

    lead_id = fields.Many2one('crm.lead')
    stage_id = fields.Many2one('crm.case.stage', string="Stage")
    item_id = fields.Many2one('crm.lead.check.list.item')
    is_done = fields.Boolean(default=False)