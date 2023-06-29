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


class PaymentBankTransferCodeData(object):
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
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PaymentBankTransferCodeData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this PaymentBankTransferCodeData.  # noqa: E501

        The financial institution's branch identification number that is associated with the lender.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :return: The id of this PaymentBankTransferCodeData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentBankTransferCodeData.

        The financial institution's branch identification number that is associated with the lender.<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul>  # noqa: E501

        :param id: The id of this PaymentBankTransferCodeData.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this PaymentBankTransferCodeData.  # noqa: E501

        The payment bank transfer code type varies based on the region of the account originates from. <br>Valid Values: BSB, IFSC, ROUTING_NUMBER, SORT_CODE<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The type of this PaymentBankTransferCodeData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentBankTransferCodeData.

        The payment bank transfer code type varies based on the region of the account originates from. <br>Valid Values: BSB, IFSC, ROUTING_NUMBER, SORT_CODE<br><b>Endpoints</b>:<ul><li>GET /partner/paymentProcessor/account</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param type: The type of this PaymentBankTransferCodeData.  # noqa: E501
        :type type: str
        """
        allowed_values = ["BSB", "IFSC", "ROUTING_NUMBER", "SORT_CODE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, PaymentBankTransferCodeData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentBankTransferCodeData):
            return True

        return self.to_dict() != other.to_dict()