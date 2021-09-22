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

from yodlee.configuration import Configuration


class UserRegistration(object):
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
        'preferences': 'UserRequestPreferences',
        'address': 'UserAddress',
        'login_name': 'str',
        'name': 'Name',
        'email': 'str',
        'segment_name': 'str'
    }

    attribute_map = {
        'preferences': 'preferences',
        'address': 'address',
        'login_name': 'loginName',
        'name': 'name',
        'email': 'email',
        'segment_name': 'segmentName'
    }

    def __init__(self, preferences=None, address=None, login_name=None, name=None, email=None, segment_name=None, _configuration=None):  # noqa: E501
        """UserRegistration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._preferences = None
        self._address = None
        self._login_name = None
        self._name = None
        self._email = None
        self._segment_name = None
        self.discriminator = None

        if preferences is not None:
            self.preferences = preferences
        if address is not None:
            self.address = address
        self.login_name = login_name
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if segment_name is not None:
            self.segment_name = segment_name

    @property
    def preferences(self):
        """Gets the preferences of this UserRegistration.  # noqa: E501


        :return: The preferences of this UserRegistration.  # noqa: E501
        :rtype: UserRequestPreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this UserRegistration.


        :param preferences: The preferences of this UserRegistration.  # noqa: E501
        :type: UserRequestPreferences
        """

        self._preferences = preferences

    @property
    def address(self):
        """Gets the address of this UserRegistration.  # noqa: E501


        :return: The address of this UserRegistration.  # noqa: E501
        :rtype: UserAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UserRegistration.


        :param address: The address of this UserRegistration.  # noqa: E501
        :type: UserAddress
        """

        self._address = address

    @property
    def login_name(self):
        """Gets the login_name of this UserRegistration.  # noqa: E501


        :return: The login_name of this UserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this UserRegistration.


        :param login_name: The login_name of this UserRegistration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and login_name is None:
            raise ValueError("Invalid value for `login_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                login_name is not None and len(login_name) > 150):
            raise ValueError("Invalid value for `login_name`, length must be less than or equal to `150`")  # noqa: E501
        if (self._configuration.client_side_validation and
                login_name is not None and len(login_name) < 3):
            raise ValueError("Invalid value for `login_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._login_name = login_name

    @property
    def name(self):
        """Gets the name of this UserRegistration.  # noqa: E501


        :return: The name of this UserRegistration.  # noqa: E501
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserRegistration.


        :param name: The name of this UserRegistration.  # noqa: E501
        :type: Name
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserRegistration.  # noqa: E501


        :return: The email of this UserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserRegistration.


        :param email: The email of this UserRegistration.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def segment_name(self):
        """Gets the segment_name of this UserRegistration.  # noqa: E501


        :return: The segment_name of this UserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._segment_name

    @segment_name.setter
    def segment_name(self, segment_name):
        """Sets the segment_name of this UserRegistration.


        :param segment_name: The segment_name of this UserRegistration.  # noqa: E501
        :type: str
        """

        self._segment_name = segment_name

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
        if issubclass(UserRegistration, dict):
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
        if not isinstance(other, UserRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRegistration):
            return True

        return self.to_dict() != other.to_dict()