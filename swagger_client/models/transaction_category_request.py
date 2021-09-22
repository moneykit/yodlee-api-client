# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yodlee_client.configuration import Configuration


class TransactionCategoryRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parent_category_id': 'int',
        'source': 'str',
        'category_name': 'str'
    }

    attribute_map = {
        'parent_category_id': 'parentCategoryId',
        'source': 'source',
        'category_name': 'categoryName'
    }

    def __init__(self, parent_category_id=None, source=None, category_name=None, _configuration=None):  # noqa: E501
        """TransactionCategoryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parent_category_id = None
        self._source = None
        self._category_name = None
        self.discriminator = None

        self.parent_category_id = parent_category_id
        if source is not None:
            self.source = source
        if category_name is not None:
            self.category_name = category_name

    @property
    def parent_category_id(self):
        """Gets the parent_category_id of this TransactionCategoryRequest.  # noqa: E501


        :return: The parent_category_id of this TransactionCategoryRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, parent_category_id):
        """Sets the parent_category_id of this TransactionCategoryRequest.


        :param parent_category_id: The parent_category_id of this TransactionCategoryRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and parent_category_id is None:
            raise ValueError("Invalid value for `parent_category_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                parent_category_id is not None and parent_category_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `parent_category_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._parent_category_id = parent_category_id

    @property
    def source(self):
        """Gets the source of this TransactionCategoryRequest.  # noqa: E501


        :return: The source of this TransactionCategoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TransactionCategoryRequest.


        :param source: The source of this TransactionCategoryRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def category_name(self):
        """Gets the category_name of this TransactionCategoryRequest.  # noqa: E501


        :return: The category_name of this TransactionCategoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this TransactionCategoryRequest.


        :param category_name: The category_name of this TransactionCategoryRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                category_name is not None and len(category_name) > 50):
            raise ValueError("Invalid value for `category_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                category_name is not None and len(category_name) < 1):
            raise ValueError("Invalid value for `category_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._category_name = category_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TransactionCategoryRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionCategoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionCategoryRequest):
            return True

        return self.to_dict() != other.to_dict()
