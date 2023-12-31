# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from yodlee.configuration import Configuration


class FullAccountNumbers(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'payment_account_number': 'str',
        'unmasked_account_number': 'str'
    }

    attribute_map = {
        'payment_account_number': 'paymentAccountNumber',
        'unmasked_account_number': 'unmaskedAccountNumber'
    }

    def __init__(self, payment_account_number=None, unmasked_account_number=None, local_vars_configuration=None):  # noqa: E501
        """FullAccountNumbers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._payment_account_number = None
        self._unmasked_account_number = None
        self.discriminator = None

        if payment_account_number is not None:
            self.payment_account_number = payment_account_number
        if unmasked_account_number is not None:
            self.unmasked_account_number = unmasked_account_number

    @property
    def payment_account_number(self):
        """Gets the payment_account_number of this FullAccountNumbers.  # noqa: E501

        The payment account number is used for payments in all regions, this may be looked as an ACH account number in the US.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :return: The payment_account_number of this FullAccountNumbers.  # noqa: E501
        :rtype: str
        """
        return self._payment_account_number

    @payment_account_number.setter
    def payment_account_number(self, payment_account_number):
        """Sets the payment_account_number of this FullAccountNumbers.

        The payment account number is used for payments in all regions, this may be looked as an ACH account number in the US.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :param payment_account_number: The payment_account_number of this FullAccountNumbers.  # noqa: E501
        :type payment_account_number: str
        """

        self._payment_account_number = payment_account_number

    @property
    def unmasked_account_number(self):
        """Gets the unmasked_account_number of this FullAccountNumbers.  # noqa: E501

        The unmasked account number is same as account number that is used to refer to an account and is not partial or masked.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :return: The unmasked_account_number of this FullAccountNumbers.  # noqa: E501
        :rtype: str
        """
        return self._unmasked_account_number

    @unmasked_account_number.setter
    def unmasked_account_number(self, unmasked_account_number):
        """Sets the unmasked_account_number of this FullAccountNumbers.

        The unmasked account number is same as account number that is used to refer to an account and is not partial or masked.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :param unmasked_account_number: The unmasked_account_number of this FullAccountNumbers.  # noqa: E501
        :type unmasked_account_number: str
        """

        self._unmasked_account_number = unmasked_account_number

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullAccountNumbers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAccountNumbers):
            return True

        return self.to_dict() != other.to_dict()
