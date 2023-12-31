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


class ClassificationSummaryTransactionSummary(object):
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
        'from_date': 'str',
        'card_payments': 'bool',
        'is_primary_account': 'bool',
        'loan_payments': 'bool',
        'to_date': 'str',
        'bill_payments': 'bool',
        'mortgage_payments': 'bool',
        'salary_credits': 'bool',
        'is_active_account': 'bool',
        'latest_transactions': 'list[ClassificationSummaryTransaction]',
        'income_credits': 'bool'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'card_payments': 'cardPayments',
        'is_primary_account': 'isPrimaryAccount',
        'loan_payments': 'loanPayments',
        'to_date': 'toDate',
        'bill_payments': 'billPayments',
        'mortgage_payments': 'mortgagePayments',
        'salary_credits': 'salaryCredits',
        'is_active_account': 'isActiveAccount',
        'latest_transactions': 'latestTransactions',
        'income_credits': 'incomeCredits'
    }

    def __init__(self, from_date=None, card_payments=None, is_primary_account=None, loan_payments=None, to_date=None, bill_payments=None, mortgage_payments=None, salary_credits=None, is_active_account=None, latest_transactions=None, income_credits=None, local_vars_configuration=None):  # noqa: E501
        """ClassificationSummaryTransactionSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_date = None
        self._card_payments = None
        self._is_primary_account = None
        self._loan_payments = None
        self._to_date = None
        self._bill_payments = None
        self._mortgage_payments = None
        self._salary_credits = None
        self._is_active_account = None
        self._latest_transactions = None
        self._income_credits = None
        self.discriminator = None

        if from_date is not None:
            self.from_date = from_date
        if card_payments is not None:
            self.card_payments = card_payments
        if is_primary_account is not None:
            self.is_primary_account = is_primary_account
        if loan_payments is not None:
            self.loan_payments = loan_payments
        if to_date is not None:
            self.to_date = to_date
        if bill_payments is not None:
            self.bill_payments = bill_payments
        if mortgage_payments is not None:
            self.mortgage_payments = mortgage_payments
        if salary_credits is not None:
            self.salary_credits = salary_credits
        if is_active_account is not None:
            self.is_active_account = is_active_account
        if latest_transactions is not None:
            self.latest_transactions = latest_transactions
        if income_credits is not None:
            self.income_credits = income_credits

    @property
    def from_date(self):
        """Gets the from_date of this ClassificationSummaryTransactionSummary.  # noqa: E501

        The date from which the transactions are considered for evaluating the attributes (Date of the oldest transaction for the accountId)  # noqa: E501

        :return: The from_date of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ClassificationSummaryTransactionSummary.

        The date from which the transactions are considered for evaluating the attributes (Date of the oldest transaction for the accountId)  # noqa: E501

        :param from_date: The from_date of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type from_date: str
        """

        self._from_date = from_date

    @property
    def card_payments(self):
        """Gets the card_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has any card-related payments based on an implicit logic  # noqa: E501

        :return: The card_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._card_payments

    @card_payments.setter
    def card_payments(self, card_payments):
        """Sets the card_payments of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has any card-related payments based on an implicit logic  # noqa: E501

        :param card_payments: The card_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type card_payments: bool
        """

        self._card_payments = card_payments

    @property
    def is_primary_account(self):
        """Gets the is_primary_account of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account is a primary account based on an implicit logic  # noqa: E501

        :return: The is_primary_account of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_account

    @is_primary_account.setter
    def is_primary_account(self, is_primary_account):
        """Sets the is_primary_account of this ClassificationSummaryTransactionSummary.

        Indicates whether the account is a primary account based on an implicit logic  # noqa: E501

        :param is_primary_account: The is_primary_account of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type is_primary_account: bool
        """

        self._is_primary_account = is_primary_account

    @property
    def loan_payments(self):
        """Gets the loan_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has any loan payments based on an implicit logic  # noqa: E501

        :return: The loan_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._loan_payments

    @loan_payments.setter
    def loan_payments(self, loan_payments):
        """Sets the loan_payments of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has any loan payments based on an implicit logic  # noqa: E501

        :param loan_payments: The loan_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type loan_payments: bool
        """

        self._loan_payments = loan_payments

    @property
    def to_date(self):
        """Gets the to_date of this ClassificationSummaryTransactionSummary.  # noqa: E501

        The date until which the transactions are considered for evaluating the attributes (Date of the latest transaction for the accountId)  # noqa: E501

        :return: The to_date of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ClassificationSummaryTransactionSummary.

        The date until which the transactions are considered for evaluating the attributes (Date of the latest transaction for the accountId)  # noqa: E501

        :param to_date: The to_date of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type to_date: str
        """

        self._to_date = to_date

    @property
    def bill_payments(self):
        """Gets the bill_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has any bill payments based on an implicit logic  # noqa: E501

        :return: The bill_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._bill_payments

    @bill_payments.setter
    def bill_payments(self, bill_payments):
        """Sets the bill_payments of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has any bill payments based on an implicit logic  # noqa: E501

        :param bill_payments: The bill_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type bill_payments: bool
        """

        self._bill_payments = bill_payments

    @property
    def mortgage_payments(self):
        """Gets the mortgage_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has any mortgage payments based on an implicit logic  # noqa: E501

        :return: The mortgage_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._mortgage_payments

    @mortgage_payments.setter
    def mortgage_payments(self, mortgage_payments):
        """Sets the mortgage_payments of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has any mortgage payments based on an implicit logic  # noqa: E501

        :param mortgage_payments: The mortgage_payments of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type mortgage_payments: bool
        """

        self._mortgage_payments = mortgage_payments

    @property
    def salary_credits(self):
        """Gets the salary_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has salary credits based on an implicit logic  # noqa: E501

        :return: The salary_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._salary_credits

    @salary_credits.setter
    def salary_credits(self, salary_credits):
        """Sets the salary_credits of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has salary credits based on an implicit logic  # noqa: E501

        :param salary_credits: The salary_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type salary_credits: bool
        """

        self._salary_credits = salary_credits

    @property
    def is_active_account(self):
        """Gets the is_active_account of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account is an active account based on an implicit logic  # noqa: E501

        :return: The is_active_account of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_active_account

    @is_active_account.setter
    def is_active_account(self, is_active_account):
        """Sets the is_active_account of this ClassificationSummaryTransactionSummary.

        Indicates whether the account is an active account based on an implicit logic  # noqa: E501

        :param is_active_account: The is_active_account of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type is_active_account: bool
        """

        self._is_active_account = is_active_account

    @property
    def latest_transactions(self):
        """Gets the latest_transactions of this ClassificationSummaryTransactionSummary.  # noqa: E501

        An array that lists the details about the latest 3 transactions that occurred in the user's account  # noqa: E501

        :return: The latest_transactions of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: list[ClassificationSummaryTransaction]
        """
        return self._latest_transactions

    @latest_transactions.setter
    def latest_transactions(self, latest_transactions):
        """Sets the latest_transactions of this ClassificationSummaryTransactionSummary.

        An array that lists the details about the latest 3 transactions that occurred in the user's account  # noqa: E501

        :param latest_transactions: The latest_transactions of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type latest_transactions: list[ClassificationSummaryTransaction]
        """

        self._latest_transactions = latest_transactions

    @property
    def income_credits(self):
        """Gets the income_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501

        Indicates whether the account has any income credits based on an implicit logic  # noqa: E501

        :return: The income_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._income_credits

    @income_credits.setter
    def income_credits(self, income_credits):
        """Sets the income_credits of this ClassificationSummaryTransactionSummary.

        Indicates whether the account has any income credits based on an implicit logic  # noqa: E501

        :param income_credits: The income_credits of this ClassificationSummaryTransactionSummary.  # noqa: E501
        :type income_credits: bool
        """

        self._income_credits = income_credits

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
        if not isinstance(other, ClassificationSummaryTransactionSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassificationSummaryTransactionSummary):
            return True

        return self.to_dict() != other.to_dict()
