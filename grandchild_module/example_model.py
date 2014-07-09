# -*- encoding: utf-8 -*-

from openerp.osv import orm, fields


class example_model(orm.Model):
    _name = 'example.model'
    _columns = {
        'name': fields.char('Name'),
    }
