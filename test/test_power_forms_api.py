# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import docusign_esign
from docusign_esign.rest import ApiException
from docusign_esign.apis.power_forms_api import PowerFormsApi


class TestPowerFormsApi(unittest.TestCase):
    """ PowerFormsApi unit test stubs """

    def setUp(self):
        self.api = docusign_esign.apis.power_forms_api.PowerFormsApi()

    def tearDown(self):
        pass

    def test_create_power_form(self):
        """
        Test case for create_power_form

        Creates a new PowerForm.
        """
        pass

    def test_delete_power_form(self):
        """
        Test case for delete_power_form

        Delete a PowerForm.
        """
        pass

    def test_delete_power_forms(self):
        """
        Test case for delete_power_forms

        Deletes one or more PowerForms
        """
        pass

    def test_get_power_form(self):
        """
        Test case for get_power_form

        Returns a single PowerForm.
        """
        pass

    def test_get_power_form_data(self):
        """
        Test case for get_power_form_data

        Returns the form data associated with the usage of a PowerForm.
        """
        pass

    def test_list_power_form_senders(self):
        """
        Test case for list_power_form_senders

        Returns the list of PowerForms available to the user.
        """
        pass

    def test_list_power_forms(self):
        """
        Test case for list_power_forms

        Returns the list of PowerForms available to the user.
        """
        pass

    def test_update_power_form(self):
        """
        Test case for update_power_form

        Creates a new PowerForm.
        """
        pass


if __name__ == '__main__':
    unittest.main()
