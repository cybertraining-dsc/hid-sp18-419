# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VMTags(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, items=None, fingerprint=None):  # noqa: E501
        """VMTags - a model defined in Swagger

        :param items: The items of this VMTags.  # noqa: E501
        :type items: List[str]
        :param fingerprint: The fingerprint of this VMTags.  # noqa: E501
        :type fingerprint: str
        """
        self.swagger_types = {
            'items': List[str],
            'fingerprint': str
        }

        self.attribute_map = {
            'items': 'items',
            'fingerprint': 'fingerprint'
        }

        self._items = items
        self._fingerprint = fingerprint

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VM_tags of this VMTags.  # noqa: E501
        :rtype: VMTags
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self):
        """Gets the items of this VMTags.


        :return: The items of this VMTags.
        :rtype: List[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this VMTags.


        :param items: The items of this VMTags.
        :type items: List[str]
        """

        self._items = items

    @property
    def fingerprint(self):
        """Gets the fingerprint of this VMTags.


        :return: The fingerprint of this VMTags.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this VMTags.


        :param fingerprint: The fingerprint of this VMTags.
        :type fingerprint: str
        """

        self._fingerprint = fingerprint
