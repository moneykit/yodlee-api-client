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


class Description(object):
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
        'security': 'str',
        'original': 'str',
        'simple': 'str',
        'consumer': 'str'
    }

    attribute_map = {
        'security': 'security',
        'original': 'original',
        'simple': 'simple',
        'consumer': 'consumer'
    }

    def __init__(self, security=None, original=None, simple=None, consumer=None, local_vars_configuration=None):  # noqa: E501
        """Description - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._security = None
        self._original = None
        self._simple = None
        self._consumer = None
        self.discriminator = None

        if security is not None:
            self.security = security
        if original is not None:
            self.original = original
        if simple is not None:
            self.simple = simple
        if consumer is not None:
            self.consumer = consumer

    @property
    def security(self):
        """Gets the security of this Description.  # noqa: E501

        The description will provide the actual name of the security.<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :return: The security of this Description.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this Description.

        The description will provide the actual name of the security.<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :param security: The security of this Description.  # noqa: E501
        :type security: str
        """

        self._security = security

    @property
    def original(self):
        """Gets the original of this Description.  # noqa: E501

        Original transaction description as it appears at the FI site.<br><br><b>Applicable containers</b>: creditCard, insurance, loan<br>  # noqa: E501

        :return: The original of this Description.  # noqa: E501
        :rtype: str
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this Description.

        Original transaction description as it appears at the FI site.<br><br><b>Applicable containers</b>: creditCard, insurance, loan<br>  # noqa: E501

        :param original: The original of this Description.  # noqa: E501
        :type original: str
        """

        self._original = original

    @property
    def simple(self):
        """Gets the simple of this Description.  # noqa: E501

        The transaction description that appears at the FI site may not be self-explanatory, i.e., the source, purpose of the transaction may not be evident. Yodlee attempts to simplify and make the transaction meaningful to the consumer, and this simplified transaction description is provided in the simple description field.Note: The simple description field is available only in the United States, Canada, United Kingdom, and India.<br><br><b>Applicable containers</b>: creditCard, insurance, loan<br>  # noqa: E501

        :return: The simple of this Description.  # noqa: E501
        :rtype: str
        """
        return self._simple

    @simple.setter
    def simple(self, simple):
        """Sets the simple of this Description.

        The transaction description that appears at the FI site may not be self-explanatory, i.e., the source, purpose of the transaction may not be evident. Yodlee attempts to simplify and make the transaction meaningful to the consumer, and this simplified transaction description is provided in the simple description field.Note: The simple description field is available only in the United States, Canada, United Kingdom, and India.<br><br><b>Applicable containers</b>: creditCard, insurance, loan<br>  # noqa: E501

        :param simple: The simple of this Description.  # noqa: E501
        :type simple: str
        """

        self._simple = simple

    @property
    def consumer(self):
        """Gets the consumer of this Description.  # noqa: E501

        The description of the transaction as defined by the consumer. The consumer can define or provide more details of the transaction in this field.<br><br>  # noqa: E501

        :return: The consumer of this Description.  # noqa: E501
        :rtype: str
        """
        return self._consumer

    @consumer.setter
    def consumer(self, consumer):
        """Sets the consumer of this Description.

        The description of the transaction as defined by the consumer. The consumer can define or provide more details of the transaction in this field.<br><br>  # noqa: E501

        :param consumer: The consumer of this Description.  # noqa: E501
        :type consumer: str
        """

        self._consumer = consumer

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
        if not isinstance(other, Description):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Description):
            return True

        return self.to_dict() != other.to_dict()
