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


class RewardBalance(object):
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
        'expiry_date': 'str',
        'balance_to_reward': 'str',
        'balance_type': 'str',
        'balance': 'float',
        'description': 'str',
        'balance_to_level': 'str',
        'units': 'str'
    }

    attribute_map = {
        'expiry_date': 'expiryDate',
        'balance_to_reward': 'balanceToReward',
        'balance_type': 'balanceType',
        'balance': 'balance',
        'description': 'description',
        'balance_to_level': 'balanceToLevel',
        'units': 'units'
    }

    def __init__(self, expiry_date=None, balance_to_reward=None, balance_type=None, balance=None, description=None, balance_to_level=None, units=None, local_vars_configuration=None):  # noqa: E501
        """RewardBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._expiry_date = None
        self._balance_to_reward = None
        self._balance_type = None
        self._balance = None
        self._description = None
        self._balance_to_level = None
        self._units = None
        self.discriminator = None

        if expiry_date is not None:
            self.expiry_date = expiry_date
        if balance_to_reward is not None:
            self.balance_to_reward = balance_to_reward
        if balance_type is not None:
            self.balance_type = balance_type
        if balance is not None:
            self.balance = balance
        if description is not None:
            self.description = description
        if balance_to_level is not None:
            self.balance_to_level = balance_to_level
        if units is not None:
            self.units = units

    @property
    def expiry_date(self):
        """Gets the expiry_date of this RewardBalance.  # noqa: E501

        The date on which the balance expires.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The expiry_date of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this RewardBalance.

        The date on which the balance expires.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param expiry_date: The expiry_date of this RewardBalance.  # noqa: E501
        :type expiry_date: str
        """

        self._expiry_date = expiry_date

    @property
    def balance_to_reward(self):
        """Gets the balance_to_reward of this RewardBalance.  # noqa: E501

        The balance required to qualify for a reward such as retaining membership, business reward, etc.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The balance_to_reward of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._balance_to_reward

    @balance_to_reward.setter
    def balance_to_reward(self, balance_to_reward):
        """Sets the balance_to_reward of this RewardBalance.

        The balance required to qualify for a reward such as retaining membership, business reward, etc.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param balance_to_reward: The balance_to_reward of this RewardBalance.  # noqa: E501
        :type balance_to_reward: str
        """

        self._balance_to_reward = balance_to_reward

    @property
    def balance_type(self):
        """Gets the balance_type of this RewardBalance.  # noqa: E501

        The type of reward balance.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The balance_type of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this RewardBalance.

        The type of reward balance.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param balance_type: The balance_type of this RewardBalance.  # noqa: E501
        :type balance_type: str
        """
        allowed_values = ["EXPIRING_BALANCE", "BALANCE_TO_LEVEL", "BALANCE_TO_REWARD", "BALANCE", "TOTAL_BALANCE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and balance_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `balance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(balance_type, allowed_values)
            )

        self._balance_type = balance_type

    @property
    def balance(self):
        """Gets the balance of this RewardBalance.  # noqa: E501

        The actual reward balance.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The balance of this RewardBalance.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this RewardBalance.

        The actual reward balance.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param balance: The balance of this RewardBalance.  # noqa: E501
        :type balance: float
        """

        self._balance = balance

    @property
    def description(self):
        """Gets the description of this RewardBalance.  # noqa: E501

        The description for the reward balance as available at provider source.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The description of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RewardBalance.

        The description for the reward balance as available at provider source.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param description: The description of this RewardBalance.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def balance_to_level(self):
        """Gets the balance_to_level of this RewardBalance.  # noqa: E501

        The balance required to reach a reward level.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The balance_to_level of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._balance_to_level

    @balance_to_level.setter
    def balance_to_level(self, balance_to_level):
        """Sets the balance_to_level of this RewardBalance.

        The balance required to reach a reward level.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param balance_to_level: The balance_to_level of this RewardBalance.  # noqa: E501
        :type balance_to_level: str
        """

        self._balance_to_level = balance_to_level

    @property
    def units(self):
        """Gets the units of this RewardBalance.  # noqa: E501

        Unit of reward balance - miles, points, segments, dollars, credits.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The units of this RewardBalance.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this RewardBalance.

        Unit of reward balance - miles, points, segments, dollars, credits.<br><br><b>Account Type</b>: Aggregated<br><b>Applicable containers</b>: reward<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param units: The units of this RewardBalance.  # noqa: E501
        :type units: str
        """

        self._units = units

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
        if not isinstance(other, RewardBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RewardBalance):
            return True

        return self.to_dict() != other.to_dict()
