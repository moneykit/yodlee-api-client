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


class VerificationAccount(object):
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
        'account_name': 'str',
        'account_type': 'str',
        'account_number': 'str',
        'user_classification': 'str',
        'bank_transfer_code': 'VerificationBankTransferCode'
    }

    attribute_map = {
        'account_name': 'accountName',
        'account_type': 'accountType',
        'account_number': 'accountNumber',
        'user_classification': 'userClassification',
        'bank_transfer_code': 'bankTransferCode'
    }

    def __init__(self, account_name=None, account_type=None, account_number=None, user_classification=None, bank_transfer_code=None, local_vars_configuration=None):  # noqa: E501
        """VerificationAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_name = None
        self._account_type = None
        self._account_number = None
        self._user_classification = None
        self._bank_transfer_code = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        self.account_type = account_type
        self.account_number = account_number
        if user_classification is not None:
            self.user_classification = user_classification
        self.bank_transfer_code = bank_transfer_code

    @property
    def account_name(self):
        """Gets the account_name of this VerificationAccount.  # noqa: E501


        :return: The account_name of this VerificationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this VerificationAccount.


        :param account_name: The account_name of this VerificationAccount.  # noqa: E501
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def account_type(self):
        """Gets the account_type of this VerificationAccount.  # noqa: E501


        :return: The account_type of this VerificationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this VerificationAccount.


        :param account_type: The account_type of this VerificationAccount.  # noqa: E501
        :type account_type: str
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SAVINGS", "CHECKING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def account_number(self):
        """Gets the account_number of this VerificationAccount.  # noqa: E501


        :return: The account_number of this VerificationAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this VerificationAccount.


        :param account_number: The account_number of this VerificationAccount.  # noqa: E501
        :type account_number: str
        """
        if self.local_vars_configuration.client_side_validation and account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) > 17):
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) < 3):
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `3`")  # noqa: E501

        self._account_number = account_number

    @property
    def user_classification(self):
        """Gets the user_classification of this VerificationAccount.  # noqa: E501


        :return: The user_classification of this VerificationAccount.  # noqa: E501
        :rtype: str
        """
        return self._user_classification

    @user_classification.setter
    def user_classification(self, user_classification):
        """Sets the user_classification of this VerificationAccount.


        :param user_classification: The user_classification of this VerificationAccount.  # noqa: E501
        :type user_classification: str
        """
        allowed_values = ["BUSINESS", "PERSONAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_classification not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_classification` ({0}), must be one of {1}"  # noqa: E501
                .format(user_classification, allowed_values)
            )

        self._user_classification = user_classification

    @property
    def bank_transfer_code(self):
        """Gets the bank_transfer_code of this VerificationAccount.  # noqa: E501


        :return: The bank_transfer_code of this VerificationAccount.  # noqa: E501
        :rtype: VerificationBankTransferCode
        """
        return self._bank_transfer_code

    @bank_transfer_code.setter
    def bank_transfer_code(self, bank_transfer_code):
        """Sets the bank_transfer_code of this VerificationAccount.


        :param bank_transfer_code: The bank_transfer_code of this VerificationAccount.  # noqa: E501
        :type bank_transfer_code: VerificationBankTransferCode
        """
        if self.local_vars_configuration.client_side_validation and bank_transfer_code is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_transfer_code`, must not be `None`")  # noqa: E501

        self._bank_transfer_code = bank_transfer_code

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
        if not isinstance(other, VerificationAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerificationAccount):
            return True

        return self.to_dict() != other.to_dict()
