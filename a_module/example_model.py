# -*- encoding: utf-8 -*-

from openerp.osv import fields, orm


class example_model(orm.Model):
    _inherit = 'example.model'
    _columns = {
        'required_field': fields.char('Required Field', required=True),
    }
