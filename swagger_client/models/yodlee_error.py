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


class YodleeError(object):
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
        'error_message': 'str',
        'error_code': 'str',
        'reference_code': 'str'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'reference_code': 'referenceCode'
    }

    def __init__(self, error_message=None, error_code=None, reference_code=None, _configuration=None):  # noqa: E501
        """YodleeError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

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
        :type: str
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
        :type: str
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
        :type: str
        """

        self._reference_code = reference_code

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
        if issubclass(YodleeError, dict):
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
        if not isinstance(other, YodleeError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, YodleeError):
            return True

        return self.to_dict() != other.to_dict()
