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


class AccountDataset(object):
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
        'last_updated': 'str',
        'update_eligibility': 'str',
        'additional_status': 'str',
        'next_update_scheduled': 'str',
        'name': 'str',
        'last_update_attempt': 'str'
    }

    attribute_map = {
        'last_updated': 'lastUpdated',
        'update_eligibility': 'updateEligibility',
        'additional_status': 'additionalStatus',
        'next_update_scheduled': 'nextUpdateScheduled',
        'name': 'name',
        'last_update_attempt': 'lastUpdateAttempt'
    }

    def __init__(self, last_updated=None, update_eligibility=None, additional_status=None, next_update_scheduled=None, name=None, last_update_attempt=None, _configuration=None):  # noqa: E501
        """AccountDataset - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_updated = None
        self._update_eligibility = None
        self._additional_status = None
        self._next_update_scheduled = None
        self._name = None
        self._last_update_attempt = None
        self.discriminator = None

        if last_updated is not None:
            self.last_updated = last_updated
        if update_eligibility is not None:
            self.update_eligibility = update_eligibility
        if additional_status is not None:
            self.additional_status = additional_status
        if next_update_scheduled is not None:
            self.next_update_scheduled = next_update_scheduled
        if name is not None:
            self.name = name
        if last_update_attempt is not None:
            self.last_update_attempt = last_update_attempt

    @property
    def last_updated(self):
        """Gets the last_updated of this AccountDataset.  # noqa: E501

        Indicate when the dataset is last updated successfully for the given provider account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The last_updated of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this AccountDataset.

        Indicate when the dataset is last updated successfully for the given provider account.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param last_updated: The last_updated of this AccountDataset.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def update_eligibility(self):
        """Gets the update_eligibility of this AccountDataset.  # noqa: E501

        Indicate whether the dataset is eligible for update or not.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The update_eligibility of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._update_eligibility

    @update_eligibility.setter
    def update_eligibility(self, update_eligibility):
        """Sets the update_eligibility of this AccountDataset.

        Indicate whether the dataset is eligible for update or not.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param update_eligibility: The update_eligibility of this AccountDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOW_UPDATE", "ALLOW_UPDATE_WITH_CREDENTIALS", "DISALLOW_UPDATE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                update_eligibility not in allowed_values):
            raise ValueError(
                "Invalid value for `update_eligibility` ({0}), must be one of {1}"  # noqa: E501
                .format(update_eligibility, allowed_values)
            )

        self._update_eligibility = update_eligibility

    @property
    def additional_status(self):
        """Gets the additional_status of this AccountDataset.  # noqa: E501

        The status of last update attempted for the dataset. <br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The additional_status of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._additional_status

    @additional_status.setter
    def additional_status(self, additional_status):
        """Sets the additional_status of this AccountDataset.

        The status of last update attempted for the dataset. <br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param additional_status: The additional_status of this AccountDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOGIN_IN_PROGRESS", "DATA_RETRIEVAL_IN_PROGRESS", "ACCT_SUMMARY_RECEIVED", "AVAILABLE_DATA_RETRIEVED", "PARTIAL_DATA_RETRIEVED", "DATA_RETRIEVAL_FAILED", "DATA_NOT_AVAILABLE", "ACCOUNT_LOCKED", "ADDL_AUTHENTICATION_REQUIRED", "BETA_SITE_DEV_IN_PROGRESS", "CREDENTIALS_UPDATE_NEEDED", "INCORRECT_CREDENTIALS", "PROPERTY_VALUE_NOT_AVAILABLE", "INVALID_ADDL_INFO_PROVIDED", "REQUEST_TIME_OUT", "SITE_BLOCKING_ERROR", "UNEXPECTED_SITE_ERROR", "SITE_NOT_SUPPORTED", "SITE_UNAVAILABLE", "TECH_ERROR", "USER_ACTION_NEEDED_AT_SITE", "SITE_SESSION_INVALIDATED", "NEW_AUTHENTICATION_REQUIRED", "DATASET_NOT_SUPPORTED", "ENROLLMENT_REQUIRED_FOR_DATASET", "CONSENT_REQUIRED", "CONSENT_EXPIRED", "CONSENT_REVOKED", "INCORRECT_OAUTH_TOKEN", "MIGRATION_IN_PROGRESS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                additional_status not in allowed_values):
            raise ValueError(
                "Invalid value for `additional_status` ({0}), must be one of {1}"  # noqa: E501
                .format(additional_status, allowed_values)
            )

        self._additional_status = additional_status

    @property
    def next_update_scheduled(self):
        """Gets the next_update_scheduled of this AccountDataset.  # noqa: E501

        Indicates when the next attempt to update the dataset is scheduled.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The next_update_scheduled of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._next_update_scheduled

    @next_update_scheduled.setter
    def next_update_scheduled(self, next_update_scheduled):
        """Sets the next_update_scheduled of this AccountDataset.

        Indicates when the next attempt to update the dataset is scheduled.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param next_update_scheduled: The next_update_scheduled of this AccountDataset.  # noqa: E501
        :type: str
        """

        self._next_update_scheduled = next_update_scheduled

    @property
    def name(self):
        """Gets the name of this AccountDataset.  # noqa: E501

        The name of the dataset requested from the provider site<br><br><b>Account Type</b>: Manual<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li><li>GET providers</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The name of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountDataset.

        The name of the dataset requested from the provider site<br><br><b>Account Type</b>: Manual<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li><li>GET providers</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param name: The name of this AccountDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["BASIC_AGG_DATA", "ADVANCE_AGG_DATA", "ACCT_PROFILE", "DOCUMENT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                name not in allowed_values):
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def last_update_attempt(self):
        """Gets the last_update_attempt of this AccountDataset.  # noqa: E501

        Indicate when the last attempt was performed to update the dataset for the given provider account<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The last_update_attempt of this AccountDataset.  # noqa: E501
        :rtype: str
        """
        return self._last_update_attempt

    @last_update_attempt.setter
    def last_update_attempt(self, last_update_attempt):
        """Sets the last_update_attempt of this AccountDataset.

        Indicate when the last attempt was performed to update the dataset for the given provider account<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param last_update_attempt: The last_update_attempt of this AccountDataset.  # noqa: E501
        :type: str
        """

        self._last_update_attempt = last_update_attempt

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
        if issubclass(AccountDataset, dict):
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
        if not isinstance(other, AccountDataset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDataset):
            return True

        return self.to_dict() != other.to_dict()
