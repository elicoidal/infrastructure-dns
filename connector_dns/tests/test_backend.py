# -*- coding: utf-8 -*-
# Copyright 2015 Elico Corp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import openerp.tests.common as common
from openerp.addons.connector.backend import Backend


class TestDNSBackend(common.TransactionCase):
    """
    Test DNS Backend
    """

    def setUp(self):
        super(TestDNSBackend, self).setUp()
        self.service = "dns"

    def test_backend(self):
        backend = Backend(self.service)
        self.assertEqual(backend.service, self.service)

    def test_child_backend(self):
        backend = Backend(self.service)
        child_backend = Backend(parent=backend, version=self.service)
        self.assertEqual(child_backend.service, backend.service)
