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


class TransactionCategorizationRule(object):
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
        'rule_clauses': 'list[RuleClause]',
        'user_defined_rule_id': 'int',
        'category_level_id': 'int',
        'transaction_categorisation_id': 'int',
        'mem_id': 'int',
        'rule_priority': 'int'
    }

    attribute_map = {
        'rule_clauses': 'ruleClauses',
        'user_defined_rule_id': 'userDefinedRuleId',
        'category_level_id': 'categoryLevelId',
        'transaction_categorisation_id': 'transactionCategorisationId',
        'mem_id': 'memId',
        'rule_priority': 'rulePriority'
    }

    def __init__(self, rule_clauses=None, user_defined_rule_id=None, category_level_id=None, transaction_categorisation_id=None, mem_id=None, rule_priority=None, _configuration=None):  # noqa: E501
        """TransactionCategorizationRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rule_clauses = None
        self._user_defined_rule_id = None
        self._category_level_id = None
        self._transaction_categorisation_id = None
        self._mem_id = None
        self._rule_priority = None
        self.discriminator = None

        if rule_clauses is not None:
            self.rule_clauses = rule_clauses
        if user_defined_rule_id is not None:
            self.user_defined_rule_id = user_defined_rule_id
        if category_level_id is not None:
            self.category_level_id = category_level_id
        if transaction_categorisation_id is not None:
            self.transaction_categorisation_id = transaction_categorisation_id
        if mem_id is not None:
            self.mem_id = mem_id
        if rule_priority is not None:
            self.rule_priority = rule_priority

    @property
    def rule_clauses(self):
        """Gets the rule_clauses of this TransactionCategorizationRule.  # noqa: E501

        Details of rules. <br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :return: The rule_clauses of this TransactionCategorizationRule.  # noqa: E501
        :rtype: list[RuleClause]
        """
        return self._rule_clauses

    @rule_clauses.setter
    def rule_clauses(self, rule_clauses):
        """Sets the rule_clauses of this TransactionCategorizationRule.

        Details of rules. <br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :param rule_clauses: The rule_clauses of this TransactionCategorizationRule.  # noqa: E501
        :type: list[RuleClause]
        """

        self._rule_clauses = rule_clauses

    @property
    def user_defined_rule_id(self):
        """Gets the user_defined_rule_id of this TransactionCategorizationRule.  # noqa: E501

        Unique identifier generated for every rule the user creates.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :return: The user_defined_rule_id of this TransactionCategorizationRule.  # noqa: E501
        :rtype: int
        """
        return self._user_defined_rule_id

    @user_defined_rule_id.setter
    def user_defined_rule_id(self, user_defined_rule_id):
        """Sets the user_defined_rule_id of this TransactionCategorizationRule.

        Unique identifier generated for every rule the user creates.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :param user_defined_rule_id: The user_defined_rule_id of this TransactionCategorizationRule.  # noqa: E501
        :type: int
        """

        self._user_defined_rule_id = user_defined_rule_id

    @property
    def category_level_id(self):
        """Gets the category_level_id of this TransactionCategorizationRule.  # noqa: E501

        The level of the category for which the rule is created.<br><br><b>Applicable containers</b>: bill, creditCard, insurance, loan<br>  # noqa: E501

        :return: The category_level_id of this TransactionCategorizationRule.  # noqa: E501
        :rtype: int
        """
        return self._category_level_id

    @category_level_id.setter
    def category_level_id(self, category_level_id):
        """Sets the category_level_id of this TransactionCategorizationRule.

        The level of the category for which the rule is created.<br><br><b>Applicable containers</b>: bill, creditCard, insurance, loan<br>  # noqa: E501

        :param category_level_id: The category_level_id of this TransactionCategorizationRule.  # noqa: E501
        :type: int
        """

        self._category_level_id = category_level_id

    @property
    def transaction_categorisation_id(self):
        """Gets the transaction_categorisation_id of this TransactionCategorizationRule.  # noqa: E501

        Category id that is assigned to the transaction when the transaction matches the rule clause. This is the id field of the transaction category resource.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :return: The transaction_categorisation_id of this TransactionCategorizationRule.  # noqa: E501
        :rtype: int
        """
        return self._transaction_categorisation_id

    @transaction_categorisation_id.setter
    def transaction_categorisation_id(self, transaction_categorisation_id):
        """Sets the transaction_categorisation_id of this TransactionCategorizationRule.

        Category id that is assigned to the transaction when the transaction matches the rule clause. This is the id field of the transaction category resource.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :param transaction_categorisation_id: The transaction_categorisation_id of this TransactionCategorizationRule.  # noqa: E501
        :type: int
        """

        self._transaction_categorisation_id = transaction_categorisation_id

    @property
    def mem_id(self):
        """Gets the mem_id of this TransactionCategorizationRule.  # noqa: E501

        Unique identifier of the user.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :return: The mem_id of this TransactionCategorizationRule.  # noqa: E501
        :rtype: int
        """
        return self._mem_id

    @mem_id.setter
    def mem_id(self, mem_id):
        """Sets the mem_id of this TransactionCategorizationRule.

        Unique identifier of the user.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :param mem_id: The mem_id of this TransactionCategorizationRule.  # noqa: E501
        :type: int
        """

        self._mem_id = mem_id

    @property
    def rule_priority(self):
        """Gets the rule_priority of this TransactionCategorizationRule.  # noqa: E501

        The order in which the rules get executed on transactions.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :return: The rule_priority of this TransactionCategorizationRule.  # noqa: E501
        :rtype: int
        """
        return self._rule_priority

    @rule_priority.setter
    def rule_priority(self, rule_priority):
        """Sets the rule_priority of this TransactionCategorizationRule.

        The order in which the rules get executed on transactions.<br><br><b>Applicable containers</b>: bill, creditCard, investment, insurance, loan<br>  # noqa: E501

        :param rule_priority: The rule_priority of this TransactionCategorizationRule.  # noqa: E501
        :type: int
        """

        self._rule_priority = rule_priority

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
        if issubclass(TransactionCategorizationRule, dict):
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
        if not isinstance(other, TransactionCategorizationRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionCategorizationRule):
            return True

        return self.to_dict() != other.to_dict()
