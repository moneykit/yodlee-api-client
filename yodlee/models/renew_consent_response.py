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


class RenewConsentResponse(object):
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
        'consent_id': 'int',
        'authorization_url': 'str',
        'provider_id': 'int'
    }

    attribute_map = {
        'consent_id': 'consentId',
        'authorization_url': 'authorizationUrl',
        'provider_id': 'providerId'
    }

    def __init__(self, consent_id=None, authorization_url=None, provider_id=None, local_vars_configuration=None):  # noqa: E501
        """RenewConsentResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._consent_id = None
        self._authorization_url = None
        self._provider_id = None
        self.discriminator = None

        if consent_id is not None:
            self.consent_id = consent_id
        if authorization_url is not None:
            self.authorization_url = authorization_url
        if provider_id is not None:
            self.provider_id = provider_id

    @property
    def consent_id(self):
        """Gets the consent_id of this RenewConsentResponse.  # noqa: E501

        Unique identifier for consent. This is created during consent creation.  # noqa: E501

        :return: The consent_id of this RenewConsentResponse.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this RenewConsentResponse.

        Unique identifier for consent. This is created during consent creation.  # noqa: E501

        :param consent_id: The consent_id of this RenewConsentResponse.  # noqa: E501
        :type consent_id: int
        """

        self._consent_id = consent_id

    @property
    def authorization_url(self):
        """Gets the authorization_url of this RenewConsentResponse.  # noqa: E501

        Authorization url generated for the request through PUT Consent to reach endsite.  # noqa: E501

        :return: The authorization_url of this RenewConsentResponse.  # noqa: E501
        :rtype: str
        """
        return self._authorization_url

    @authorization_url.setter
    def authorization_url(self, authorization_url):
        """Sets the authorization_url of this RenewConsentResponse.

        Authorization url generated for the request through PUT Consent to reach endsite.  # noqa: E501

        :param authorization_url: The authorization_url of this RenewConsentResponse.  # noqa: E501
        :type authorization_url: str
        """

        self._authorization_url = authorization_url

    @property
    def provider_id(self):
        """Gets the provider_id of this RenewConsentResponse.  # noqa: E501

        Unique identifier for the provider account resource. This is created during account addition.  # noqa: E501

        :return: The provider_id of this RenewConsentResponse.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this RenewConsentResponse.

        Unique identifier for the provider account resource. This is created during account addition.  # noqa: E501

        :param provider_id: The provider_id of this RenewConsentResponse.  # noqa: E501
        :type provider_id: int
        """

        self._provider_id = provider_id

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
        if not isinstance(other, RenewConsentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenewConsentResponse):
            return True

        return self.to_dict() != other.to_dict()
