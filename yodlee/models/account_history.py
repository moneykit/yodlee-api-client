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


class AccountHistory(object):
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
        'historical_balances': 'list[HistoricalBalance]',
        'id': 'int'
    }

    attribute_map = {
        'historical_balances': 'historicalBalances',
        'id': 'id'
    }

    def __init__(self, historical_balances=None, id=None, local_vars_configuration=None):  # noqa: E501
        """AccountHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._historical_balances = None
        self._id = None
        self.discriminator = None

        if historical_balances is not None:
            self.historical_balances = historical_balances
        if id is not None:
            self.id = id

    @property
    def historical_balances(self):
        """Gets the historical_balances of this AccountHistory.  # noqa: E501


        :return: The historical_balances of this AccountHistory.  # noqa: E501
        :rtype: list[HistoricalBalance]
        """
        return self._historical_balances

    @historical_balances.setter
    def historical_balances(self, historical_balances):
        """Sets the historical_balances of this AccountHistory.


        :param historical_balances: The historical_balances of this AccountHistory.  # noqa: E501
        :type historical_balances: list[HistoricalBalance]
        """

        self._historical_balances = historical_balances

    @property
    def id(self):
        """Gets the id of this AccountHistory.  # noqa: E501


        :return: The id of this AccountHistory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountHistory.


        :param id: The id of this AccountHistory.  # noqa: E501
        :type id: int
        """

        self._id = id

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
        if not isinstance(other, AccountHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHistory):
            return True

        return self.to_dict() != other.to_dict()
