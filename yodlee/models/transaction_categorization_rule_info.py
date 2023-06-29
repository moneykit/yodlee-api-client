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


class TransactionCategorizationRuleInfo(object):
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
        'rule_clause': 'list[FieldOperation]',
        'source': 'str',
        'priority': 'int',
        'category_id': 'int'
    }

    attribute_map = {
        'rule_clause': 'ruleClause',
        'source': 'source',
        'priority': 'priority',
        'category_id': 'categoryId'
    }

    def __init__(self, rule_clause=None, source=None, priority=None, category_id=None, local_vars_configuration=None):  # noqa: E501
        """TransactionCategorizationRuleInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_clause = None
        self._source = None
        self._priority = None
        self._category_id = None
        self.discriminator = None

        self.rule_clause = rule_clause
        if source is not None:
            self.source = source
        if priority is not None:
            self.priority = priority
        self.category_id = category_id

    @property
    def rule_clause(self):
        """Gets the rule_clause of this TransactionCategorizationRuleInfo.  # noqa: E501


        :return: The rule_clause of this TransactionCategorizationRuleInfo.  # noqa: E501
        :rtype: list[FieldOperation]
        """
        return self._rule_clause

    @rule_clause.setter
    def rule_clause(self, rule_clause):
        """Sets the rule_clause of this TransactionCategorizationRuleInfo.


        :param rule_clause: The rule_clause of this TransactionCategorizationRuleInfo.  # noqa: E501
        :type rule_clause: list[FieldOperation]
        """
        if self.local_vars_configuration.client_side_validation and rule_clause is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_clause`, must not be `None`")  # noqa: E501

        self._rule_clause = rule_clause

    @property
    def source(self):
        """Gets the source of this TransactionCategorizationRuleInfo.  # noqa: E501


        :return: The source of this TransactionCategorizationRuleInfo.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TransactionCategorizationRuleInfo.


        :param source: The source of this TransactionCategorizationRuleInfo.  # noqa: E501
        :type source: str
        """
        allowed_values = ["SYSTEM", "USER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def priority(self):
        """Gets the priority of this TransactionCategorizationRuleInfo.  # noqa: E501


        :return: The priority of this TransactionCategorizationRuleInfo.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TransactionCategorizationRuleInfo.


        :param priority: The priority of this TransactionCategorizationRuleInfo.  # noqa: E501
        :type priority: int
        """

        self._priority = priority

    @property
    def category_id(self):
        """Gets the category_id of this TransactionCategorizationRuleInfo.  # noqa: E501


        :return: The category_id of this TransactionCategorizationRuleInfo.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this TransactionCategorizationRuleInfo.


        :param category_id: The category_id of this TransactionCategorizationRuleInfo.  # noqa: E501
        :type category_id: int
        """
        if self.local_vars_configuration.client_side_validation and category_id is None:  # noqa: E501
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

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
        if not isinstance(other, TransactionCategorizationRuleInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionCategorizationRuleInfo):
            return True

        return self.to_dict() != other.to_dict()
