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


class RenewalConsent(object):
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
        'default_renewal_duration': 'str',
        'is_reauthorization_required': 'bool'
    }

    attribute_map = {
        'default_renewal_duration': 'defaultRenewalDuration',
        'is_reauthorization_required': 'isReauthorizationRequired'
    }

    def __init__(self, default_renewal_duration=None, is_reauthorization_required=None, local_vars_configuration=None):  # noqa: E501
        """RenewalConsent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._default_renewal_duration = None
        self._is_reauthorization_required = None
        self.discriminator = None

        if default_renewal_duration is not None:
            self.default_renewal_duration = default_renewal_duration
        if is_reauthorization_required is not None:
            self.is_reauthorization_required = is_reauthorization_required

    @property
    def default_renewal_duration(self):
        """Gets the default_renewal_duration of this RenewalConsent.  # noqa: E501

        Consent default renewal duration.<br><br><b>Endpoints</b>:<ul><li>PUT consents/{consentId}/renewal</li></ul>  # noqa: E501

        :return: The default_renewal_duration of this RenewalConsent.  # noqa: E501
        :rtype: str
        """
        return self._default_renewal_duration

    @default_renewal_duration.setter
    def default_renewal_duration(self, default_renewal_duration):
        """Sets the default_renewal_duration of this RenewalConsent.

        Consent default renewal duration.<br><br><b>Endpoints</b>:<ul><li>PUT consents/{consentId}/renewal</li></ul>  # noqa: E501

        :param default_renewal_duration: The default_renewal_duration of this RenewalConsent.  # noqa: E501
        :type default_renewal_duration: str
        """

        self._default_renewal_duration = default_renewal_duration

    @property
    def is_reauthorization_required(self):
        """Gets the is_reauthorization_required of this RenewalConsent.  # noqa: E501

        Consent eligibility for reauthorization.<br><br><b>Endpoints</b>:<ul><li>PUT consents/{consentId}/renewal</li></ul>  # noqa: E501

        :return: The is_reauthorization_required of this RenewalConsent.  # noqa: E501
        :rtype: bool
        """
        return self._is_reauthorization_required

    @is_reauthorization_required.setter
    def is_reauthorization_required(self, is_reauthorization_required):
        """Sets the is_reauthorization_required of this RenewalConsent.

        Consent eligibility for reauthorization.<br><br><b>Endpoints</b>:<ul><li>PUT consents/{consentId}/renewal</li></ul>  # noqa: E501

        :param is_reauthorization_required: The is_reauthorization_required of this RenewalConsent.  # noqa: E501
        :type is_reauthorization_required: bool
        """

        self._is_reauthorization_required = is_reauthorization_required

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
        if not isinstance(other, RenewalConsent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenewalConsent):
            return True

        return self.to_dict() != other.to_dict()
