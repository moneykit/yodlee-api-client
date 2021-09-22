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

from yodlee.configuration import Configuration


class CoverageAmount(object):
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
        'cover': 'Money',
        'unit_type': 'str',
        'type': 'str',
        'limit_type': 'str',
        'met': 'Money'
    }

    attribute_map = {
        'cover': 'cover',
        'unit_type': 'unitType',
        'type': 'type',
        'limit_type': 'limitType',
        'met': 'met'
    }

    def __init__(self, cover=None, unit_type=None, type=None, limit_type=None, met=None, _configuration=None):  # noqa: E501
        """CoverageAmount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cover = None
        self._unit_type = None
        self._type = None
        self._limit_type = None
        self._met = None
        self.discriminator = None

        if cover is not None:
            self.cover = cover
        if unit_type is not None:
            self.unit_type = unit_type
        if type is not None:
            self.type = type
        if limit_type is not None:
            self.limit_type = limit_type
        if met is not None:
            self.met = met

    @property
    def cover(self):
        """Gets the cover of this CoverageAmount.  # noqa: E501

        The maximum amount that will be paid to an individual or an entity for a covered loss<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The cover of this CoverageAmount.  # noqa: E501
        :rtype: Money
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """Sets the cover of this CoverageAmount.

        The maximum amount that will be paid to an individual or an entity for a covered loss<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param cover: The cover of this CoverageAmount.  # noqa: E501
        :type: Money
        """

        self._cover = cover

    @property
    def unit_type(self):
        """Gets the unit_type of this CoverageAmount.  # noqa: E501

        The type of coverage unit indicates if the coverage is for an individual or a family.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :return: The unit_type of this CoverageAmount.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this CoverageAmount.

        The type of coverage unit indicates if the coverage is for an individual or a family.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :param unit_type: The unit_type of this CoverageAmount.  # noqa: E501
        :type: str
        """
        allowed_values = ["PER_FAMILY", "PER_MEMBER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                unit_type not in allowed_values):
            raise ValueError(
                "Invalid value for `unit_type` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_type, allowed_values)
            )

        self._unit_type = unit_type

    @property
    def type(self):
        """Gets the type of this CoverageAmount.  # noqa: E501

        The type of coverage provided to an individual or an entity.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :return: The type of this CoverageAmount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoverageAmount.

        The type of coverage provided to an individual or an entity.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :param type: The type of this CoverageAmount.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEDUCTIBLE", "OUT_OF_POCKET", "ANNUAL_BENEFIT", "MAX_BENEFIT", "COVERAGE_AMOUNT", "MONTHLY_BENEFIT", "OTHER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def limit_type(self):
        """Gets the limit_type of this CoverageAmount.  # noqa: E501

        The type of coverage limit indicates if the coverage is in-network or out-of-network.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :return: The limit_type of this CoverageAmount.  # noqa: E501
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        """Sets the limit_type of this CoverageAmount.

        The type of coverage limit indicates if the coverage is in-network or out-of-network.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul><b>Applicable Values:</b><br>  # noqa: E501

        :param limit_type: The limit_type of this CoverageAmount.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_NETWORK", "OUT_NETWORK"]  # noqa: E501
        if (self._configuration.client_side_validation and
                limit_type not in allowed_values):
            raise ValueError(
                "Invalid value for `limit_type` ({0}), must be one of {1}"  # noqa: E501
                .format(limit_type, allowed_values)
            )

        self._limit_type = limit_type

    @property
    def met(self):
        """Gets the met of this CoverageAmount.  # noqa: E501

        The amount the insurance company paid for the incurred medical expenses.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :return: The met of this CoverageAmount.  # noqa: E501
        :rtype: Money
        """
        return self._met

    @met.setter
    def met(self, met):
        """Sets the met of this CoverageAmount.

        The amount the insurance company paid for the incurred medical expenses.<br><br><b>Aggregated / Manual</b>: Aggregated<br><b>Applicable containers</b>: insurance,investment<br><b>Endpoints</b>:<ul><li>GET accounts</li><li>GET accounts/{accountId}</li></ul>  # noqa: E501

        :param met: The met of this CoverageAmount.  # noqa: E501
        :type: Money
        """

        self._met = met

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
        if issubclass(CoverageAmount, dict):
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
        if not isinstance(other, CoverageAmount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoverageAmount):
            return True

        return self.to_dict() != other.to_dict()