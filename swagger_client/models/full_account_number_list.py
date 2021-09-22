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


class FullAccountNumberList(object):
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
        'payment_account_number': 'str',
        'unmasked_account_number': 'str'
    }

    attribute_map = {
        'payment_account_number': 'paymentAccountNumber',
        'unmasked_account_number': 'unmaskedAccountNumber'
    }

    def __init__(self, payment_account_number=None, unmasked_account_number=None, _configuration=None):  # noqa: E501
        """FullAccountNumberList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payment_account_number = None
        self._unmasked_account_number = None
        self.discriminator = None

        if payment_account_number is not None:
            self.payment_account_number = payment_account_number
        if unmasked_account_number is not None:
            self.unmasked_account_number = unmasked_account_number

    @property
    def payment_account_number(self):
        """Gets the payment_account_number of this FullAccountNumberList.  # noqa: E501

        Payment Account Number of given account.<br><br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The payment_account_number of this FullAccountNumberList.  # noqa: E501
        :rtype: str
        """
        return self._payment_account_number

    @payment_account_number.setter
    def payment_account_number(self, payment_account_number):
        """Sets the payment_account_number of this FullAccountNumberList.

        Payment Account Number of given account.<br><br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param payment_account_number: The payment_account_number of this FullAccountNumberList.  # noqa: E501
        :type: str
        """

        self._payment_account_number = payment_account_number

    @property
    def unmasked_account_number(self):
        """Gets the unmasked_account_number of this FullAccountNumberList.  # noqa: E501

        Unmasked account number of given account.<br><br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The unmasked_account_number of this FullAccountNumberList.  # noqa: E501
        :rtype: str
        """
        return self._unmasked_account_number

    @unmasked_account_number.setter
    def unmasked_account_number(self, unmasked_account_number):
        """Sets the unmasked_account_number of this FullAccountNumberList.

        Unmasked account number of given account.<br><br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param unmasked_account_number: The unmasked_account_number of this FullAccountNumberList.  # noqa: E501
        :type: str
        """

        self._unmasked_account_number = unmasked_account_number

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
        if issubclass(FullAccountNumberList, dict):
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
        if not isinstance(other, FullAccountNumberList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAccountNumberList):
            return True

        return self.to_dict() != other.to_dict()
