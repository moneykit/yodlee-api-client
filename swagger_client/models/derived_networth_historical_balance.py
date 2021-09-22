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


class DerivedNetworthHistoricalBalance(object):
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
        '_date': 'str',
        'account_id': 'int',
        'is_asset': 'bool',
        'balance': 'Money',
        'as_of_date': 'str',
        'data_source_type': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'account_id': 'accountId',
        'is_asset': 'isAsset',
        'balance': 'balance',
        'as_of_date': 'asOfDate',
        'data_source_type': 'dataSourceType'
    }

    def __init__(self, _date=None, account_id=None, is_asset=None, balance=None, as_of_date=None, data_source_type=None, _configuration=None):  # noqa: E501
        """DerivedNetworthHistoricalBalance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._account_id = None
        self._is_asset = None
        self._balance = None
        self._as_of_date = None
        self._data_source_type = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if account_id is not None:
            self.account_id = account_id
        if is_asset is not None:
            self.is_asset = is_asset
        if balance is not None:
            self.balance = balance
        if as_of_date is not None:
            self.as_of_date = as_of_date
        if data_source_type is not None:
            self.data_source_type = data_source_type

    @property
    def _date(self):
        """Gets the _date of this DerivedNetworthHistoricalBalance.  # noqa: E501

        Date for which the account balance was provided.  This balance could be a carryforward, calculated or a scraped balance. AdditIonal Details: scraped: Balance shown in the provider site. This balance gets stored in Yodlee system during system/user account updates. carryForward : Balance carried forward from the scraped balance to the days for which the balance was not available in the system. Balance may not be available for all the days in the system due to MFA information required, error in the site, credential changes, etc. calculated: Balances that gets calculated for the days that are prior to the account added date.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li><li>GET derived/networth</li></ul>  # noqa: E501

        :return: The _date of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DerivedNetworthHistoricalBalance.

        Date for which the account balance was provided.  This balance could be a carryforward, calculated or a scraped balance. AdditIonal Details: scraped: Balance shown in the provider site. This balance gets stored in Yodlee system during system/user account updates. carryForward : Balance carried forward from the scraped balance to the days for which the balance was not available in the system. Balance may not be available for all the days in the system due to MFA information required, error in the site, credential changes, etc. calculated: Balances that gets calculated for the days that are prior to the account added date.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li><li>GET derived/networth</li></ul>  # noqa: E501

        :param _date: The _date of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def account_id(self):
        """Gets the account_id of this DerivedNetworthHistoricalBalance.  # noqa: E501


        :return: The account_id of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DerivedNetworthHistoricalBalance.


        :param account_id: The account_id of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def is_asset(self):
        """Gets the is_asset of this DerivedNetworthHistoricalBalance.  # noqa: E501

        Indicates whether the balance is an asset or liability.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :return: The is_asset of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: bool
        """
        return self._is_asset

    @is_asset.setter
    def is_asset(self, is_asset):
        """Sets the is_asset of this DerivedNetworthHistoricalBalance.

        Indicates whether the balance is an asset or liability.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :param is_asset: The is_asset of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: bool
        """

        self._is_asset = is_asset

    @property
    def balance(self):
        """Gets the balance of this DerivedNetworthHistoricalBalance.  # noqa: E501

        Balance amount of the account.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :return: The balance of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: Money
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this DerivedNetworthHistoricalBalance.

        Balance amount of the account.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :param balance: The balance of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: Money
        """

        self._balance = balance

    @property
    def as_of_date(self):
        """Gets the as_of_date of this DerivedNetworthHistoricalBalance.  # noqa: E501

        Date as of when the balance is last  updated due to the auto account updates or user triggered updates. This balance will be carry forward for the days where there is no balance available in the system. <br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :return: The as_of_date of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self._as_of_date

    @as_of_date.setter
    def as_of_date(self, as_of_date):
        """Sets the as_of_date of this DerivedNetworthHistoricalBalance.

        Date as of when the balance is last  updated due to the auto account updates or user triggered updates. This balance will be carry forward for the days where there is no balance available in the system. <br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul>  # noqa: E501

        :param as_of_date: The as_of_date of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: str
        """

        self._as_of_date = as_of_date

    @property
    def data_source_type(self):
        """Gets the data_source_type of this DerivedNetworthHistoricalBalance.  # noqa: E501

        The source of balance information.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The data_source_type of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this DerivedNetworthHistoricalBalance.

        The source of balance information.<br><br><b>Account Type</b>: Aggregated and Manual<br><b>Applicable containers</b>: bank, creditCard, investment, insurance, realEstate, loan<br><b>Endpoints</b>:<ul><li>GET accounts/historicalBalances</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param data_source_type: The data_source_type of this DerivedNetworthHistoricalBalance.  # noqa: E501
        :type: str
        """
        allowed_values = ["S", "C", "CF"]  # noqa: E501
        if (self._configuration.client_side_validation and
                data_source_type not in allowed_values):
            raise ValueError(
                "Invalid value for `data_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_source_type, allowed_values)
            )

        self._data_source_type = data_source_type

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
        if issubclass(DerivedNetworthHistoricalBalance, dict):
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
        if not isinstance(other, DerivedNetworthHistoricalBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivedNetworthHistoricalBalance):
            return True

        return self.to_dict() != other.to_dict()
