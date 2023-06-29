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


class DerivedHoldingSummaryResponse(object):
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
        'holding_summary': 'list[DerivedHoldingsSummary]',
        'link': 'DerivedHoldingsLinks'
    }

    attribute_map = {
        'holding_summary': 'holdingSummary',
        'link': 'link'
    }

    def __init__(self, holding_summary=None, link=None, local_vars_configuration=None):  # noqa: E501
        """DerivedHoldingSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._holding_summary = None
        self._link = None
        self.discriminator = None

        if holding_summary is not None:
            self.holding_summary = holding_summary
        if link is not None:
            self.link = link

    @property
    def holding_summary(self):
        """Gets the holding_summary of this DerivedHoldingSummaryResponse.  # noqa: E501


        :return: The holding_summary of this DerivedHoldingSummaryResponse.  # noqa: E501
        :rtype: list[DerivedHoldingsSummary]
        """
        return self._holding_summary

    @holding_summary.setter
    def holding_summary(self, holding_summary):
        """Sets the holding_summary of this DerivedHoldingSummaryResponse.


        :param holding_summary: The holding_summary of this DerivedHoldingSummaryResponse.  # noqa: E501
        :type holding_summary: list[DerivedHoldingsSummary]
        """

        self._holding_summary = holding_summary

    @property
    def link(self):
        """Gets the link of this DerivedHoldingSummaryResponse.  # noqa: E501


        :return: The link of this DerivedHoldingSummaryResponse.  # noqa: E501
        :rtype: DerivedHoldingsLinks
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DerivedHoldingSummaryResponse.


        :param link: The link of this DerivedHoldingSummaryResponse.  # noqa: E501
        :type link: DerivedHoldingsLinks
        """

        self._link = link

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
        if not isinstance(other, DerivedHoldingSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivedHoldingSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
