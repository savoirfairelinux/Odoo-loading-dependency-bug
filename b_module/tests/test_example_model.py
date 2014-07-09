# -*- encoding: utf-8 -*-

from openerp.tests.common import TransactionCase


class test_example_model(TransactionCase):
    def setUp(self):
        super(test_example_model, self).setUp()
        self.model = self.registry("example.model")

    def test_create(self):
        self.model.create(self.cr, self.uid, {'name': 'test'})
