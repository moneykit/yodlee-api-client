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


class AccountProfile(object):
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
        'identifier': 'list[Identifier]',
        'address': 'list[AccountAddress]',
        'phone_number': 'list[PhoneNumber]',
        'email': 'list[Email]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'address': 'address',
        'phone_number': 'phoneNumber',
        'email': 'email'
    }

    def __init__(self, identifier=None, address=None, phone_number=None, email=None, _configuration=None):  # noqa: E501
        """AccountProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identifier = None
        self._address = None
        self._phone_number = None
        self._email = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if address is not None:
            self.address = address
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email

    @property
    def identifier(self):
        """Gets the identifier of this AccountProfile.  # noqa: E501

        Identifiers available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The identifier of this AccountProfile.  # noqa: E501
        :rtype: list[Identifier]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this AccountProfile.

        Identifiers available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param identifier: The identifier of this AccountProfile.  # noqa: E501
        :type: list[Identifier]
        """

        self._identifier = identifier

    @property
    def address(self):
        """Gets the address of this AccountProfile.  # noqa: E501

        Address available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The address of this AccountProfile.  # noqa: E501
        :rtype: list[AccountAddress]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccountProfile.

        Address available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param address: The address of this AccountProfile.  # noqa: E501
        :type: list[AccountAddress]
        """

        self._address = address

    @property
    def phone_number(self):
        """Gets the phone_number of this AccountProfile.  # noqa: E501

        Phone number available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The phone_number of this AccountProfile.  # noqa: E501
        :rtype: list[PhoneNumber]
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this AccountProfile.

        Phone number available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param phone_number: The phone_number of this AccountProfile.  # noqa: E501
        :type: list[PhoneNumber]
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """Gets the email of this AccountProfile.  # noqa: E501

        Email Id available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The email of this AccountProfile.  # noqa: E501
        :rtype: list[Email]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountProfile.

        Email Id available in the profile page of the account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param email: The email of this AccountProfile.  # noqa: E501
        :type: list[Email]
        """

        self._email = email

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
        if issubclass(AccountProfile, dict):
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
        if not isinstance(other, AccountProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountProfile):
            return True

        return self.to_dict() != other.to_dict()
