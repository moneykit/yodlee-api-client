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


class YodleeError(object):
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
        'error_message': 'str',
        'error_code': 'str',
        'reference_code': 'str'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'reference_code': 'referenceCode'
    }

    def __init__(self, error_message=None, error_code=None, reference_code=None, local_vars_configuration=None):  # noqa: E501
        """YodleeError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._error_message = None
        self._error_code = None
        self._reference_code = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if reference_code is not None:
            self.reference_code = reference_code

    @property
    def error_message(self):
        """Gets the error_message of this YodleeError.  # noqa: E501


        :return: The error_message of this YodleeError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this YodleeError.


        :param error_message: The error_message of this YodleeError.  # noqa: E501
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this YodleeError.  # noqa: E501


        :return: The error_code of this YodleeError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this YodleeError.


        :param error_code: The error_code of this YodleeError.  # noqa: E501
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def reference_code(self):
        """Gets the reference_code of this YodleeError.  # noqa: E501


        :return: The reference_code of this YodleeError.  # noqa: E501
        :rtype: str
        """
        return self._reference_code

    @reference_code.setter
    def reference_code(self, reference_code):
        """Sets the reference_code of this YodleeError.


        :param reference_code: The reference_code of this YodleeError.  # noqa: E501
        :type reference_code: str
        """

        self._reference_code = reference_code

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
        if not isinstance(other, YodleeError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, YodleeError):
            return True

        return self.to_dict() != other.to_dict()
