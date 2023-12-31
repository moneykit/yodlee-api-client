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


class ProviderAccountRequest(object):
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
        'consent_id': 'int',
        'preferences': 'ProviderAccountPreferences',
        'aggregation_source': 'str',
        'field': 'list[Field]',
        'dataset_name': 'list[str]',
        'dataset': 'list[ProvidersDataset]'
    }

    attribute_map = {
        'consent_id': 'consentId',
        'preferences': 'preferences',
        'aggregation_source': 'aggregationSource',
        'field': 'field',
        'dataset_name': 'datasetName',
        'dataset': 'dataset'
    }

    def __init__(self, consent_id=None, preferences=None, aggregation_source=None, field=None, dataset_name=None, dataset=None, local_vars_configuration=None):  # noqa: E501
        """ProviderAccountRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._consent_id = None
        self._preferences = None
        self._aggregation_source = None
        self._field = None
        self._dataset_name = None
        self._dataset = None
        self.discriminator = None

        if consent_id is not None:
            self.consent_id = consent_id
        if preferences is not None:
            self.preferences = preferences
        if aggregation_source is not None:
            self.aggregation_source = aggregation_source
        self.field = field
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset is not None:
            self.dataset = dataset

    @property
    def consent_id(self):
        """Gets the consent_id of this ProviderAccountRequest.  # noqa: E501

        Consent Id generated for the request through POST Consent.<br><br><b>Endpoints</b>:<ul><li>POST Provider Account</li><li>PUT Provider Account</li></ul>  # noqa: E501

        :return: The consent_id of this ProviderAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ProviderAccountRequest.

        Consent Id generated for the request through POST Consent.<br><br><b>Endpoints</b>:<ul><li>POST Provider Account</li><li>PUT Provider Account</li></ul>  # noqa: E501

        :param consent_id: The consent_id of this ProviderAccountRequest.  # noqa: E501
        :type consent_id: int
        """

        self._consent_id = consent_id

    @property
    def preferences(self):
        """Gets the preferences of this ProviderAccountRequest.  # noqa: E501


        :return: The preferences of this ProviderAccountRequest.  # noqa: E501
        :rtype: ProviderAccountPreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this ProviderAccountRequest.


        :param preferences: The preferences of this ProviderAccountRequest.  # noqa: E501
        :type preferences: ProviderAccountPreferences
        """

        self._preferences = preferences

    @property
    def aggregation_source(self):
        """Gets the aggregation_source of this ProviderAccountRequest.  # noqa: E501


        :return: The aggregation_source of this ProviderAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_source

    @aggregation_source.setter
    def aggregation_source(self, aggregation_source):
        """Sets the aggregation_source of this ProviderAccountRequest.


        :param aggregation_source: The aggregation_source of this ProviderAccountRequest.  # noqa: E501
        :type aggregation_source: str
        """
        allowed_values = ["SYSTEM", "USER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aggregation_source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `aggregation_source` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_source, allowed_values)
            )

        self._aggregation_source = aggregation_source

    @property
    def field(self):
        """Gets the field of this ProviderAccountRequest.  # noqa: E501


        :return: The field of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[Field]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ProviderAccountRequest.


        :param field: The field of this ProviderAccountRequest.  # noqa: E501
        :type field: list[Field]
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def dataset_name(self):
        """Gets the dataset_name of this ProviderAccountRequest.  # noqa: E501


        :return: The dataset_name of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this ProviderAccountRequest.


        :param dataset_name: The dataset_name of this ProviderAccountRequest.  # noqa: E501
        :type dataset_name: list[str]
        """
        allowed_values = ["BASIC_AGG_DATA", "ADVANCE_AGG_DATA", "ACCT_PROFILE", "DOCUMENT"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(dataset_name).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `dataset_name` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(dataset_name) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._dataset_name = dataset_name

    @property
    def dataset(self):
        """Gets the dataset of this ProviderAccountRequest.  # noqa: E501


        :return: The dataset of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[ProvidersDataset]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this ProviderAccountRequest.


        :param dataset: The dataset of this ProviderAccountRequest.  # noqa: E501
        :type dataset: list[ProvidersDataset]
        """

        self._dataset = dataset

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
        if not isinstance(other, ProviderAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProviderAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
