# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectFailureFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, envelope_ids=None, synchronous=None):
        """
        ConnectFailureFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'envelope_ids': 'list[str]',
            'synchronous': 'str'
        }

        self.attribute_map = {
            'envelope_ids': 'envelopeIds',
            'synchronous': 'synchronous'
        }

        self._envelope_ids = envelope_ids
        self._synchronous = synchronous

    @property
    def envelope_ids(self):
        """
        Gets the envelope_ids of this ConnectFailureFilter.
        

        :return: The envelope_ids of this ConnectFailureFilter.
        :rtype: list[str]
        """
        return self._envelope_ids

    @envelope_ids.setter
    def envelope_ids(self, envelope_ids):
        """
        Sets the envelope_ids of this ConnectFailureFilter.
        

        :param envelope_ids: The envelope_ids of this ConnectFailureFilter.
        :type: list[str]
        """

        self._envelope_ids = envelope_ids

    @property
    def synchronous(self):
        """
        Gets the synchronous of this ConnectFailureFilter.
        

        :return: The synchronous of this ConnectFailureFilter.
        :rtype: str
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this ConnectFailureFilter.
        

        :param synchronous: The synchronous of this ConnectFailureFilter.
        :type: str
        """

        self._synchronous = synchronous

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other