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


class EvaluateAddressResponse(object):
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
        'address': 'list[AccountAddress]',
        'is_valid_address': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'is_valid_address': 'isValidAddress'
    }

    def __init__(self, address=None, is_valid_address=None, local_vars_configuration=None):  # noqa: E501
        """EvaluateAddressResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._is_valid_address = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if is_valid_address is not None:
            self.is_valid_address = is_valid_address

    @property
    def address(self):
        """Gets the address of this EvaluateAddressResponse.  # noqa: E501


        :return: The address of this EvaluateAddressResponse.  # noqa: E501
        :rtype: list[AccountAddress]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EvaluateAddressResponse.


        :param address: The address of this EvaluateAddressResponse.  # noqa: E501
        :type address: list[AccountAddress]
        """

        self._address = address

    @property
    def is_valid_address(self):
        """Gets the is_valid_address of this EvaluateAddressResponse.  # noqa: E501


        :return: The is_valid_address of this EvaluateAddressResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid_address

    @is_valid_address.setter
    def is_valid_address(self, is_valid_address):
        """Sets the is_valid_address of this EvaluateAddressResponse.


        :param is_valid_address: The is_valid_address of this EvaluateAddressResponse.  # noqa: E501
        :type is_valid_address: bool
        """

        self._is_valid_address = is_valid_address

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
        if not isinstance(other, EvaluateAddressResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EvaluateAddressResponse):
            return True

        return self.to_dict() != other.to_dict()
