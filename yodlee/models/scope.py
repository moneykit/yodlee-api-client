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


class Scope(object):
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
        'title_body': 'list[str]',
        'scope_id': 'str',
        'dataset_attributes': 'list[str]',
        'title': 'str'
    }

    attribute_map = {
        'title_body': 'titleBody',
        'scope_id': 'scopeId',
        'dataset_attributes': 'datasetAttributes',
        'title': 'title'
    }

    def __init__(self, title_body=None, scope_id=None, dataset_attributes=None, title=None, local_vars_configuration=None):  # noqa: E501
        """Scope - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._title_body = None
        self._scope_id = None
        self._dataset_attributes = None
        self._title = None
        self.discriminator = None

        self.title_body = title_body
        self.scope_id = scope_id
        if dataset_attributes is not None:
            self.dataset_attributes = dataset_attributes
        self.title = title

    @property
    def title_body(self):
        """Gets the title_body of this Scope.  # noqa: E501

        Title body that explains the purpose of the scope.  # noqa: E501

        :return: The title_body of this Scope.  # noqa: E501
        :rtype: list[str]
        """
        return self._title_body

    @title_body.setter
    def title_body(self, title_body):
        """Sets the title_body of this Scope.

        Title body that explains the purpose of the scope.  # noqa: E501

        :param title_body: The title_body of this Scope.  # noqa: E501
        :type title_body: list[str]
        """
        if self.local_vars_configuration.client_side_validation and title_body is None:  # noqa: E501
            raise ValueError("Invalid value for `title_body`, must not be `None`")  # noqa: E501

        self._title_body = title_body

    @property
    def scope_id(self):
        """Gets the scope_id of this Scope.  # noqa: E501

        Unique Dataset Cluster name for the consent group like <br/> ACCOUNT_DETAILS<br/> STATEMENT_DETAILS<br/> CONTACT_DETAILS<br/> TRANSACTION_DETAILS  # noqa: E501

        :return: The scope_id of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this Scope.

        Unique Dataset Cluster name for the consent group like <br/> ACCOUNT_DETAILS<br/> STATEMENT_DETAILS<br/> CONTACT_DETAILS<br/> TRANSACTION_DETAILS  # noqa: E501

        :param scope_id: The scope_id of this Scope.  # noqa: E501
        :type scope_id: str
        """
        if self.local_vars_configuration.client_side_validation and scope_id is None:  # noqa: E501
            raise ValueError("Invalid value for `scope_id`, must not be `None`")  # noqa: E501
        allowed_values = ["ACCOUNT_DETAILS", "TRANSACTION_DETAILS", "STATEMENT_DETAILS", "CONTACT_DETAILS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and scope_id not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `scope_id` ({0}), must be one of {1}"  # noqa: E501
                .format(scope_id, allowed_values)
            )

        self._scope_id = scope_id

    @property
    def dataset_attributes(self):
        """Gets the dataset_attributes of this Scope.  # noqa: E501

        Permissions that are associated with the Consent group like<br/> BASIC_AGG_DATA.BASIC_ACCOUNT_INFO<br/> BASIC_AGG_DATA.ACCOUNT_DETAILS<br/> BASIC_AGG_DATA.STATEMENTS<br/> BASIC_AGG_DATA.TRANSACTIONS<br/> ACCT_PROFILE.HOLDER_NAME<br/> ACCT_PROFILE.FULL_ACCT_NUMBER<br/> ACCT_PROFILE.BANK_TRANSFER_CODE<br/> ACCT_PROFILE.HOLDER_DETAILS  # noqa: E501

        :return: The dataset_attributes of this Scope.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_attributes

    @dataset_attributes.setter
    def dataset_attributes(self, dataset_attributes):
        """Sets the dataset_attributes of this Scope.

        Permissions that are associated with the Consent group like<br/> BASIC_AGG_DATA.BASIC_ACCOUNT_INFO<br/> BASIC_AGG_DATA.ACCOUNT_DETAILS<br/> BASIC_AGG_DATA.STATEMENTS<br/> BASIC_AGG_DATA.TRANSACTIONS<br/> ACCT_PROFILE.HOLDER_NAME<br/> ACCT_PROFILE.FULL_ACCT_NUMBER<br/> ACCT_PROFILE.BANK_TRANSFER_CODE<br/> ACCT_PROFILE.HOLDER_DETAILS  # noqa: E501

        :param dataset_attributes: The dataset_attributes of this Scope.  # noqa: E501
        :type dataset_attributes: list[str]
        """

        self._dataset_attributes = dataset_attributes

    @property
    def title(self):
        """Gets the title of this Scope.  # noqa: E501

        Title for the Data Cluster.  # noqa: E501

        :return: The title of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Scope.

        Title for the Data Cluster.  # noqa: E501

        :param title: The title of this Scope.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if not isinstance(other, Scope):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scope):
            return True

        return self.to_dict() != other.to_dict()
