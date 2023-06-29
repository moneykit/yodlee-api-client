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


class UserAddress(object):
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
        'zip': 'str',
        'country': 'str',
        'address3': 'str',
        'address2': 'str',
        'city': 'str',
        'address1': 'str',
        'state': 'str'
    }

    attribute_map = {
        'zip': 'zip',
        'country': 'country',
        'address3': 'address3',
        'address2': 'address2',
        'city': 'city',
        'address1': 'address1',
        'state': 'state'
    }

    def __init__(self, zip=None, country=None, address3=None, address2=None, city=None, address1=None, state=None, local_vars_configuration=None):  # noqa: E501
        """UserAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._zip = None
        self._country = None
        self._address3 = None
        self._address2 = None
        self._city = None
        self._address1 = None
        self._state = None
        self.discriminator = None

        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country
        if address3 is not None:
            self.address3 = address3
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if address1 is not None:
            self.address1 = address1
        if state is not None:
            self.state = state

    @property
    def zip(self):
        """Gets the zip of this UserAddress.  # noqa: E501


        :return: The zip of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this UserAddress.


        :param zip: The zip of this UserAddress.  # noqa: E501
        :type zip: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this UserAddress.  # noqa: E501


        :return: The country of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserAddress.


        :param country: The country of this UserAddress.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def address3(self):
        """Gets the address3 of this UserAddress.  # noqa: E501


        :return: The address3 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this UserAddress.


        :param address3: The address3 of this UserAddress.  # noqa: E501
        :type address3: str
        """

        self._address3 = address3

    @property
    def address2(self):
        """Gets the address2 of this UserAddress.  # noqa: E501


        :return: The address2 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this UserAddress.


        :param address2: The address2 of this UserAddress.  # noqa: E501
        :type address2: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this UserAddress.  # noqa: E501


        :return: The city of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this UserAddress.


        :param city: The city of this UserAddress.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def address1(self):
        """Gets the address1 of this UserAddress.  # noqa: E501


        :return: The address1 of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this UserAddress.


        :param address1: The address1 of this UserAddress.  # noqa: E501
        :type address1: str
        """

        self._address1 = address1

    @property
    def state(self):
        """Gets the state of this UserAddress.  # noqa: E501


        :return: The state of this UserAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UserAddress.


        :param state: The state of this UserAddress.  # noqa: E501
        :type state: str
        """

        self._state = state

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
        if not isinstance(other, UserAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAddress):
            return True

        return self.to_dict() != other.to_dict()
