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


class Name(object):
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
        'middle': 'str',
        'last': 'str',
        'full_name': 'str',
        'first': 'str'
    }

    attribute_map = {
        'middle': 'middle',
        'last': 'last',
        'full_name': 'fullName',
        'first': 'first'
    }

    def __init__(self, middle=None, last=None, full_name=None, first=None, local_vars_configuration=None):  # noqa: E501
        """Name - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._middle = None
        self._last = None
        self._full_name = None
        self._first = None
        self.discriminator = None

        if middle is not None:
            self.middle = middle
        if last is not None:
            self.last = last
        if full_name is not None:
            self.full_name = full_name
        if first is not None:
            self.first = first

    @property
    def middle(self):
        """Gets the middle of this Name.  # noqa: E501


        :return: The middle of this Name.  # noqa: E501
        :rtype: str
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        """Sets the middle of this Name.


        :param middle: The middle of this Name.  # noqa: E501
        :type middle: str
        """

        self._middle = middle

    @property
    def last(self):
        """Gets the last of this Name.  # noqa: E501


        :return: The last of this Name.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Name.


        :param last: The last of this Name.  # noqa: E501
        :type last: str
        """

        self._last = last

    @property
    def full_name(self):
        """Gets the full_name of this Name.  # noqa: E501


        :return: The full_name of this Name.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Name.


        :param full_name: The full_name of this Name.  # noqa: E501
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def first(self):
        """Gets the first of this Name.  # noqa: E501


        :return: The first of this Name.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Name.


        :param first: The first of this Name.  # noqa: E501
        :type first: str
        """

        self._first = first

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
        if not isinstance(other, Name):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Name):
            return True

        return self.to_dict() != other.to_dict()
