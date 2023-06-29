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


class Statement(object):
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
        'apr': 'float',
        'cash_apr': 'float',
        'billing_period_start': 'str',
        'due_date': 'str',
        'interest_amount': 'Money',
        'statement_date': 'str',
        'cash_advance': 'Money',
        'billing_period_end': 'str',
        'principal_amount': 'Money',
        'loan_balance': 'Money',
        'amount_due': 'Money',
        'account_id': 'int',
        'last_updated': 'str',
        'is_latest': 'bool',
        'minimum_payment': 'Money',
        'last_payment_date': 'str',
        'last_payment_amount': 'Money',
        'id': 'int',
        'new_charges': 'Money'
    }

    attribute_map = {
        'apr': 'apr',
        'cash_apr': 'cashApr',
        'billing_period_start': 'billingPeriodStart',
        'due_date': 'dueDate',
        'interest_amount': 'interestAmount',
        'statement_date': 'statementDate',
        'cash_advance': 'cashAdvance',
        'billing_period_end': 'billingPeriodEnd',
        'principal_amount': 'principalAmount',
        'loan_balance': 'loanBalance',
        'amount_due': 'amountDue',
        'account_id': 'accountId',
        'last_updated': 'lastUpdated',
        'is_latest': 'isLatest',
        'minimum_payment': 'minimumPayment',
        'last_payment_date': 'lastPaymentDate',
        'last_payment_amount': 'lastPaymentAmount',
        'id': 'id',
        'new_charges': 'newCharges'
    }

    def __init__(self, apr=None, cash_apr=None, billing_period_start=None, due_date=None, interest_amount=None, statement_date=None, cash_advance=None, billing_period_end=None, principal_amount=None, loan_balance=None, amount_due=None, account_id=None, last_updated=None, is_latest=None, minimum_payment=None, last_payment_date=None, last_payment_amount=None, id=None, new_charges=None, local_vars_configuration=None):  # noqa: E501
        """Statement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._apr = None
        self._cash_apr = None
        self._billing_period_start = None
        self._due_date = None
        self._interest_amount = None
        self._statement_date = None
        self._cash_advance = None
        self._billing_period_end = None
        self._principal_amount = None
        self._loan_balance = None
        self._amount_due = None
        self._account_id = None
        self._last_updated = None
        self._is_latest = None
        self._minimum_payment = None
        self._last_payment_date = None
        self._last_payment_amount = None
        self._id = None
        self._new_charges = None
        self.discriminator = None

        if apr is not None:
            self.apr = apr
        if cash_apr is not None:
            self.cash_apr = cash_apr
        if billing_period_start is not None:
            self.billing_period_start = billing_period_start
        if due_date is not None:
            self.due_date = due_date
        if interest_amount is not None:
            self.interest_amount = interest_amount
        if statement_date is not None:
            self.statement_date = statement_date
        if cash_advance is not None:
            self.cash_advance = cash_advance
        if billing_period_end is not None:
            self.billing_period_end = billing_period_end
        if principal_amount is not None:
            self.principal_amount = principal_amount
        if loan_balance is not None:
            self.loan_balance = loan_balance
        if amount_due is not None:
            self.amount_due = amount_due
        if account_id is not None:
            self.account_id = account_id
        if last_updated is not None:
            self.last_updated = last_updated
        if is_latest is not None:
            self.is_latest = is_latest
        if minimum_payment is not None:
            self.minimum_payment = minimum_payment
        if last_payment_date is not None:
            self.last_payment_date = last_payment_date
        if last_payment_amount is not None:
            self.last_payment_amount = last_payment_amount
        if id is not None:
            self.id = id
        if new_charges is not None:
            self.new_charges = new_charges

    @property
    def apr(self):
        """Gets the apr of this Statement.  # noqa: E501

        The APR applied to the balance on the credit card account, as available in the statement.<br><b>Note:</b> In case of variable APR, the APR available on the statement might differ from the APR available at the account-level.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The apr of this Statement.  # noqa: E501
        :rtype: float
        """
        return self._apr

    @apr.setter
    def apr(self, apr):
        """Sets the apr of this Statement.

        The APR applied to the balance on the credit card account, as available in the statement.<br><b>Note:</b> In case of variable APR, the APR available on the statement might differ from the APR available at the account-level.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param apr: The apr of this Statement.  # noqa: E501
        :type apr: float
        """

        self._apr = apr

    @property
    def cash_apr(self):
        """Gets the cash_apr of this Statement.  # noqa: E501

        The APR applicable to cash withdrawals on the credit card account.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The cash_apr of this Statement.  # noqa: E501
        :rtype: float
        """
        return self._cash_apr

    @cash_apr.setter
    def cash_apr(self, cash_apr):
        """Sets the cash_apr of this Statement.

        The APR applicable to cash withdrawals on the credit card account.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param cash_apr: The cash_apr of this Statement.  # noqa: E501
        :type cash_apr: float
        """

        self._cash_apr = cash_apr

    @property
    def billing_period_start(self):
        """Gets the billing_period_start of this Statement.  # noqa: E501

        The start date of the statement period.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The billing_period_start of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_start

    @billing_period_start.setter
    def billing_period_start(self, billing_period_start):
        """Sets the billing_period_start of this Statement.

        The start date of the statement period.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param billing_period_start: The billing_period_start of this Statement.  # noqa: E501
        :type billing_period_start: str
        """

        self._billing_period_start = billing_period_start

    @property
    def due_date(self):
        """Gets the due_date of this Statement.  # noqa: E501

        The date by when the minimum payment is due to be paid.<br><b>Note:</b> The due date that appears in the statement may differ from the due date at the account-level.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The due_date of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Statement.

        The date by when the minimum payment is due to be paid.<br><b>Note:</b> The due date that appears in the statement may differ from the due date at the account-level.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param due_date: The due_date of this Statement.  # noqa: E501
        :type due_date: str
        """

        self._due_date = due_date

    @property
    def interest_amount(self):
        """Gets the interest_amount of this Statement.  # noqa: E501


        :return: The interest_amount of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._interest_amount

    @interest_amount.setter
    def interest_amount(self, interest_amount):
        """Sets the interest_amount of this Statement.


        :param interest_amount: The interest_amount of this Statement.  # noqa: E501
        :type interest_amount: Money
        """

        self._interest_amount = interest_amount

    @property
    def statement_date(self):
        """Gets the statement_date of this Statement.  # noqa: E501

        The date on which the statement is generated.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The statement_date of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._statement_date

    @statement_date.setter
    def statement_date(self, statement_date):
        """Sets the statement_date of this Statement.

        The date on which the statement is generated.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param statement_date: The statement_date of this Statement.  # noqa: E501
        :type statement_date: str
        """

        self._statement_date = statement_date

    @property
    def cash_advance(self):
        """Gets the cash_advance of this Statement.  # noqa: E501


        :return: The cash_advance of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._cash_advance

    @cash_advance.setter
    def cash_advance(self, cash_advance):
        """Sets the cash_advance of this Statement.


        :param cash_advance: The cash_advance of this Statement.  # noqa: E501
        :type cash_advance: Money
        """

        self._cash_advance = cash_advance

    @property
    def billing_period_end(self):
        """Gets the billing_period_end of this Statement.  # noqa: E501

        The end date of the statement period.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The billing_period_end of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_end

    @billing_period_end.setter
    def billing_period_end(self, billing_period_end):
        """Sets the billing_period_end of this Statement.

        The end date of the statement period.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param billing_period_end: The billing_period_end of this Statement.  # noqa: E501
        :type billing_period_end: str
        """

        self._billing_period_end = billing_period_end

    @property
    def principal_amount(self):
        """Gets the principal_amount of this Statement.  # noqa: E501


        :return: The principal_amount of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, principal_amount):
        """Sets the principal_amount of this Statement.


        :param principal_amount: The principal_amount of this Statement.  # noqa: E501
        :type principal_amount: Money
        """

        self._principal_amount = principal_amount

    @property
    def loan_balance(self):
        """Gets the loan_balance of this Statement.  # noqa: E501


        :return: The loan_balance of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._loan_balance

    @loan_balance.setter
    def loan_balance(self, loan_balance):
        """Sets the loan_balance of this Statement.


        :param loan_balance: The loan_balance of this Statement.  # noqa: E501
        :type loan_balance: Money
        """

        self._loan_balance = loan_balance

    @property
    def amount_due(self):
        """Gets the amount_due of this Statement.  # noqa: E501


        :return: The amount_due of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this Statement.


        :param amount_due: The amount_due of this Statement.  # noqa: E501
        :type amount_due: Money
        """

        self._amount_due = amount_due

    @property
    def account_id(self):
        """Gets the account_id of this Statement.  # noqa: E501

        Account to which the statement belongs to.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The account_id of this Statement.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Statement.

        Account to which the statement belongs to.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param account_id: The account_id of this Statement.  # noqa: E501
        :type account_id: int
        """

        self._account_id = account_id

    @property
    def last_updated(self):
        """Gets the last_updated of this Statement.  # noqa: E501

        The date when the account was last updated by Yodlee.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The last_updated of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Statement.

        The date when the account was last updated by Yodlee.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param last_updated: The last_updated of this Statement.  # noqa: E501
        :type last_updated: str
        """

        self._last_updated = last_updated

    @property
    def is_latest(self):
        """Gets the is_latest of this Statement.  # noqa: E501

        The field is set to true if the statement is the latest generated statement.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The is_latest of this Statement.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this Statement.

        The field is set to true if the statement is the latest generated statement.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param is_latest: The is_latest of this Statement.  # noqa: E501
        :type is_latest: bool
        """

        self._is_latest = is_latest

    @property
    def minimum_payment(self):
        """Gets the minimum_payment of this Statement.  # noqa: E501


        :return: The minimum_payment of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._minimum_payment

    @minimum_payment.setter
    def minimum_payment(self, minimum_payment):
        """Sets the minimum_payment of this Statement.


        :param minimum_payment: The minimum_payment of this Statement.  # noqa: E501
        :type minimum_payment: Money
        """

        self._minimum_payment = minimum_payment

    @property
    def last_payment_date(self):
        """Gets the last_payment_date of this Statement.  # noqa: E501

        The date on which the last payment was done during the billing cycle.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The last_payment_date of this Statement.  # noqa: E501
        :rtype: str
        """
        return self._last_payment_date

    @last_payment_date.setter
    def last_payment_date(self, last_payment_date):
        """Sets the last_payment_date of this Statement.

        The date on which the last payment was done during the billing cycle.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param last_payment_date: The last_payment_date of this Statement.  # noqa: E501
        :type last_payment_date: str
        """

        self._last_payment_date = last_payment_date

    @property
    def last_payment_amount(self):
        """Gets the last_payment_amount of this Statement.  # noqa: E501


        :return: The last_payment_amount of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._last_payment_amount

    @last_payment_amount.setter
    def last_payment_amount(self, last_payment_amount):
        """Sets the last_payment_amount of this Statement.


        :param last_payment_amount: The last_payment_amount of this Statement.  # noqa: E501
        :type last_payment_amount: Money
        """

        self._last_payment_amount = last_payment_amount

    @property
    def id(self):
        """Gets the id of this Statement.  # noqa: E501

        Unique identifier for the statement.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :return: The id of this Statement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Statement.

        Unique identifier for the statement.<br><br><b>Applicable containers</b>: creditCard, loan, insurance<br>  # noqa: E501

        :param id: The id of this Statement.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def new_charges(self):
        """Gets the new_charges of this Statement.  # noqa: E501


        :return: The new_charges of this Statement.  # noqa: E501
        :rtype: Money
        """
        return self._new_charges

    @new_charges.setter
    def new_charges(self, new_charges):
        """Sets the new_charges of this Statement.


        :param new_charges: The new_charges of this Statement.  # noqa: E501
        :type new_charges: Money
        """

        self._new_charges = new_charges

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
        if not isinstance(other, Statement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Statement):
            return True

        return self.to_dict() != other.to_dict()
