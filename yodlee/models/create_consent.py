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


class CreateConsent(object):
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
        'data_access_frequency': 'str',
        'otsp_adr_name': 'str',
        'preferences': 'list[Preferences]',
        'otsp_adr': 'str',
        'client_adr': 'str',
        'renewal': 'Renewal',
        'client_trusted_advisor': 'list[ClientTrustedAdvisor]',
        'provider_consent_id': 'str',
        'revoke_date': 'str',
        'title': 'str',
        'application_display_name': 'str',
        'title_body': 'str',
        'consent_id': 'int',
        'third_party_adr': 'list[ThirdPartyADR]',
        'provider_id': 'int',
        'consent_status': 'str',
        'scope': 'list[Scope]',
        'user_data_treatment': 'UserDataTreatment',
        'start_date': 'str',
        'expiration_date': 'str'
    }

    attribute_map = {
        'data_access_frequency': 'dataAccessFrequency',
        'otsp_adr_name': 'otspADRName',
        'preferences': 'preferences',
        'otsp_adr': 'otspADR',
        'client_adr': 'clientADR',
        'renewal': 'renewal',
        'client_trusted_advisor': 'clientTrustedAdvisor',
        'provider_consent_id': 'providerConsentId',
        'revoke_date': 'revokeDate',
        'title': 'title',
        'application_display_name': 'applicationDisplayName',
        'title_body': 'titleBody',
        'consent_id': 'consentId',
        'third_party_adr': 'thirdPartyADR',
        'provider_id': 'providerId',
        'consent_status': 'consentStatus',
        'scope': 'scope',
        'user_data_treatment': 'userDataTreatment',
        'start_date': 'startDate',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, data_access_frequency=None, otsp_adr_name=None, preferences=None, otsp_adr=None, client_adr=None, renewal=None, client_trusted_advisor=None, provider_consent_id=None, revoke_date=None, title=None, application_display_name=None, title_body=None, consent_id=None, third_party_adr=None, provider_id=None, consent_status=None, scope=None, user_data_treatment=None, start_date=None, expiration_date=None, local_vars_configuration=None):  # noqa: E501
        """CreateConsent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data_access_frequency = None
        self._otsp_adr_name = None
        self._preferences = None
        self._otsp_adr = None
        self._client_adr = None
        self._renewal = None
        self._client_trusted_advisor = None
        self._provider_consent_id = None
        self._revoke_date = None
        self._title = None
        self._application_display_name = None
        self._title_body = None
        self._consent_id = None
        self._third_party_adr = None
        self._provider_id = None
        self._consent_status = None
        self._scope = None
        self._user_data_treatment = None
        self._start_date = None
        self._expiration_date = None
        self.discriminator = None

        if data_access_frequency is not None:
            self.data_access_frequency = data_access_frequency
        if otsp_adr_name is not None:
            self.otsp_adr_name = otsp_adr_name
        self.preferences = preferences
        if otsp_adr is not None:
            self.otsp_adr = otsp_adr
        self.client_adr = client_adr
        if renewal is not None:
            self.renewal = renewal
        self.client_trusted_advisor = client_trusted_advisor
        if provider_consent_id is not None:
            self.provider_consent_id = provider_consent_id
        self.revoke_date = revoke_date
        self.title = title
        self.application_display_name = application_display_name
        self.title_body = title_body
        self.consent_id = consent_id
        if third_party_adr is not None:
            self.third_party_adr = third_party_adr
        self.provider_id = provider_id
        self.consent_status = consent_status
        self.scope = scope
        if user_data_treatment is not None:
            self.user_data_treatment = user_data_treatment
        self.start_date = start_date
        self.expiration_date = expiration_date

    @property
    def data_access_frequency(self):
        """Gets the data_access_frequency of this CreateConsent.  # noqa: E501

        Data Access Frequency explains the number of times that this consent can be used.<br> Otherwise called as consent frequency type.  # noqa: E501

        :return: The data_access_frequency of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._data_access_frequency

    @data_access_frequency.setter
    def data_access_frequency(self, data_access_frequency):
        """Sets the data_access_frequency of this CreateConsent.

        Data Access Frequency explains the number of times that this consent can be used.<br> Otherwise called as consent frequency type.  # noqa: E501

        :param data_access_frequency: The data_access_frequency of this CreateConsent.  # noqa: E501
        :type data_access_frequency: str
        """
        allowed_values = ["ONE_TIME", "RECURRING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_access_frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_access_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(data_access_frequency, allowed_values)
            )

        self._data_access_frequency = data_access_frequency

    @property
    def otsp_adr_name(self):
        """Gets the otsp_adr_name of this CreateConsent.  # noqa: E501

        Name of the Accredited Data Recipient/Organization  # noqa: E501

        :return: The otsp_adr_name of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._otsp_adr_name

    @otsp_adr_name.setter
    def otsp_adr_name(self, otsp_adr_name):
        """Sets the otsp_adr_name of this CreateConsent.

        Name of the Accredited Data Recipient/Organization  # noqa: E501

        :param otsp_adr_name: The otsp_adr_name of this CreateConsent.  # noqa: E501
        :type otsp_adr_name: str
        """

        self._otsp_adr_name = otsp_adr_name

    @property
    def preferences(self):
        """Gets the preferences of this CreateConsent.  # noqa: E501

        Preferences describes options about the additional usage of data or purge data  # noqa: E501

        :return: The preferences of this CreateConsent.  # noqa: E501
        :rtype: list[Preferences]
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this CreateConsent.

        Preferences describes options about the additional usage of data or purge data  # noqa: E501

        :param preferences: The preferences of this CreateConsent.  # noqa: E501
        :type preferences: list[Preferences]
        """
        if self.local_vars_configuration.client_side_validation and preferences is None:  # noqa: E501
            raise ValueError("Invalid value for `preferences`, must not be `None`")  # noqa: E501

        self._preferences = preferences

    @property
    def otsp_adr(self):
        """Gets the otsp_adr of this CreateConsent.  # noqa: E501

        Unique/Accredition Id of the ADR  # noqa: E501

        :return: The otsp_adr of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._otsp_adr

    @otsp_adr.setter
    def otsp_adr(self, otsp_adr):
        """Sets the otsp_adr of this CreateConsent.

        Unique/Accredition Id of the ADR  # noqa: E501

        :param otsp_adr: The otsp_adr of this CreateConsent.  # noqa: E501
        :type otsp_adr: str
        """

        self._otsp_adr = otsp_adr

    @property
    def client_adr(self):
        """Gets the client_adr of this CreateConsent.  # noqa: E501

        Client Name of the ADR  # noqa: E501

        :return: The client_adr of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._client_adr

    @client_adr.setter
    def client_adr(self, client_adr):
        """Sets the client_adr of this CreateConsent.

        Client Name of the ADR  # noqa: E501

        :param client_adr: The client_adr of this CreateConsent.  # noqa: E501
        :type client_adr: str
        """
        if self.local_vars_configuration.client_side_validation and client_adr is None:  # noqa: E501
            raise ValueError("Invalid value for `client_adr`, must not be `None`")  # noqa: E501

        self._client_adr = client_adr

    @property
    def renewal(self):
        """Gets the renewal of this CreateConsent.  # noqa: E501


        :return: The renewal of this CreateConsent.  # noqa: E501
        :rtype: Renewal
        """
        return self._renewal

    @renewal.setter
    def renewal(self, renewal):
        """Sets the renewal of this CreateConsent.


        :param renewal: The renewal of this CreateConsent.  # noqa: E501
        :type renewal: Renewal
        """

        self._renewal = renewal

    @property
    def client_trusted_advisor(self):
        """Gets the client_trusted_advisor of this CreateConsent.  # noqa: E501

        describes information of client trusted advisor  # noqa: E501

        :return: The client_trusted_advisor of this CreateConsent.  # noqa: E501
        :rtype: list[ClientTrustedAdvisor]
        """
        return self._client_trusted_advisor

    @client_trusted_advisor.setter
    def client_trusted_advisor(self, client_trusted_advisor):
        """Sets the client_trusted_advisor of this CreateConsent.

        describes information of client trusted advisor  # noqa: E501

        :param client_trusted_advisor: The client_trusted_advisor of this CreateConsent.  # noqa: E501
        :type client_trusted_advisor: list[ClientTrustedAdvisor]
        """
        if self.local_vars_configuration.client_side_validation and client_trusted_advisor is None:  # noqa: E501
            raise ValueError("Invalid value for `client_trusted_advisor`, must not be `None`")  # noqa: E501

        self._client_trusted_advisor = client_trusted_advisor

    @property
    def provider_consent_id(self):
        """Gets the provider_consent_id of this CreateConsent.  # noqa: E501

        Provider consent id  # noqa: E501

        :return: The provider_consent_id of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._provider_consent_id

    @provider_consent_id.setter
    def provider_consent_id(self, provider_consent_id):
        """Sets the provider_consent_id of this CreateConsent.

        Provider consent id  # noqa: E501

        :param provider_consent_id: The provider_consent_id of this CreateConsent.  # noqa: E501
        :type provider_consent_id: str
        """

        self._provider_consent_id = provider_consent_id

    @property
    def revoke_date(self):
        """Gets the revoke_date of this CreateConsent.  # noqa: E501

        Consent revoke date.  # noqa: E501

        :return: The revoke_date of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._revoke_date

    @revoke_date.setter
    def revoke_date(self, revoke_date):
        """Sets the revoke_date of this CreateConsent.

        Consent revoke date.  # noqa: E501

        :param revoke_date: The revoke_date of this CreateConsent.  # noqa: E501
        :type revoke_date: str
        """
        if self.local_vars_configuration.client_side_validation and revoke_date is None:  # noqa: E501
            raise ValueError("Invalid value for `revoke_date`, must not be `None`")  # noqa: E501

        self._revoke_date = revoke_date

    @property
    def title(self):
        """Gets the title of this CreateConsent.  # noqa: E501

        Title for the consent form.  # noqa: E501

        :return: The title of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateConsent.

        Title for the consent form.  # noqa: E501

        :param title: The title of this CreateConsent.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def application_display_name(self):
        """Gets the application_display_name of this CreateConsent.  # noqa: E501

        Application display name.  # noqa: E501

        :return: The application_display_name of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._application_display_name

    @application_display_name.setter
    def application_display_name(self, application_display_name):
        """Sets the application_display_name of this CreateConsent.

        Application display name.  # noqa: E501

        :param application_display_name: The application_display_name of this CreateConsent.  # noqa: E501
        :type application_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and application_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `application_display_name`, must not be `None`")  # noqa: E501

        self._application_display_name = application_display_name

    @property
    def title_body(self):
        """Gets the title_body of this CreateConsent.  # noqa: E501

        Description for the title.  # noqa: E501

        :return: The title_body of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._title_body

    @title_body.setter
    def title_body(self, title_body):
        """Sets the title_body of this CreateConsent.

        Description for the title.  # noqa: E501

        :param title_body: The title_body of this CreateConsent.  # noqa: E501
        :type title_body: str
        """
        if self.local_vars_configuration.client_side_validation and title_body is None:  # noqa: E501
            raise ValueError("Invalid value for `title_body`, must not be `None`")  # noqa: E501

        self._title_body = title_body

    @property
    def consent_id(self):
        """Gets the consent_id of this CreateConsent.  # noqa: E501

        Consent Id generated through POST Consent.  # noqa: E501

        :return: The consent_id of this CreateConsent.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this CreateConsent.

        Consent Id generated through POST Consent.  # noqa: E501

        :param consent_id: The consent_id of this CreateConsent.  # noqa: E501
        :type consent_id: int
        """
        if self.local_vars_configuration.client_side_validation and consent_id is None:  # noqa: E501
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def third_party_adr(self):
        """Gets the third_party_adr of this CreateConsent.  # noqa: E501

        ThirdPartyADR describes details of additional parties which are accredited data recipients under organization  # noqa: E501

        :return: The third_party_adr of this CreateConsent.  # noqa: E501
        :rtype: list[ThirdPartyADR]
        """
        return self._third_party_adr

    @third_party_adr.setter
    def third_party_adr(self, third_party_adr):
        """Sets the third_party_adr of this CreateConsent.

        ThirdPartyADR describes details of additional parties which are accredited data recipients under organization  # noqa: E501

        :param third_party_adr: The third_party_adr of this CreateConsent.  # noqa: E501
        :type third_party_adr: list[ThirdPartyADR]
        """

        self._third_party_adr = third_party_adr

    @property
    def provider_id(self):
        """Gets the provider_id of this CreateConsent.  # noqa: E501

        Provider Id for which the consent needs to be generated.  # noqa: E501

        :return: The provider_id of this CreateConsent.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this CreateConsent.

        Provider Id for which the consent needs to be generated.  # noqa: E501

        :param provider_id: The provider_id of this CreateConsent.  # noqa: E501
        :type provider_id: int
        """
        if self.local_vars_configuration.client_side_validation and provider_id is None:  # noqa: E501
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def consent_status(self):
        """Gets the consent_status of this CreateConsent.  # noqa: E501

        Status of the consent.  # noqa: E501

        :return: The consent_status of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._consent_status

    @consent_status.setter
    def consent_status(self, consent_status):
        """Sets the consent_status of this CreateConsent.

        Status of the consent.  # noqa: E501

        :param consent_status: The consent_status of this CreateConsent.  # noqa: E501
        :type consent_status: str
        """
        if self.local_vars_configuration.client_side_validation and consent_status is None:  # noqa: E501
            raise ValueError("Invalid value for `consent_status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "CONSENT_GENERATED", "CONSENT_ACCEPTED", "CONSENT_AUTHORIZED", "CONSENT_MISMATCH", "PENDING", "EXPIRED", "REVOKED", "CONSENT_REPEALED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and consent_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `consent_status` ({0}), must be one of {1}"  # noqa: E501
                .format(consent_status, allowed_values)
            )

        self._consent_status = consent_status

    @property
    def scope(self):
        """Gets the scope of this CreateConsent.  # noqa: E501

        Scope describes about the consent permissions and their purpose.  # noqa: E501

        :return: The scope of this CreateConsent.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CreateConsent.

        Scope describes about the consent permissions and their purpose.  # noqa: E501

        :param scope: The scope of this CreateConsent.  # noqa: E501
        :type scope: list[Scope]
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def user_data_treatment(self):
        """Gets the user_data_treatment of this CreateConsent.  # noqa: E501


        :return: The user_data_treatment of this CreateConsent.  # noqa: E501
        :rtype: UserDataTreatment
        """
        return self._user_data_treatment

    @user_data_treatment.setter
    def user_data_treatment(self, user_data_treatment):
        """Sets the user_data_treatment of this CreateConsent.


        :param user_data_treatment: The user_data_treatment of this CreateConsent.  # noqa: E501
        :type user_data_treatment: UserDataTreatment
        """

        self._user_data_treatment = user_data_treatment

    @property
    def start_date(self):
        """Gets the start_date of this CreateConsent.  # noqa: E501

        Consent start date.  # noqa: E501

        :return: The start_date of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateConsent.

        Consent start date.  # noqa: E501

        :param start_date: The start_date of this CreateConsent.  # noqa: E501
        :type start_date: str
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this CreateConsent.  # noqa: E501

        Consent expiry date.  # noqa: E501

        :return: The expiration_date of this CreateConsent.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this CreateConsent.

        Consent expiry date.  # noqa: E501

        :param expiration_date: The expiration_date of this CreateConsent.  # noqa: E501
        :type expiration_date: str
        """
        if self.local_vars_configuration.client_side_validation and expiration_date is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

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
        if not isinstance(other, CreateConsent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConsent):
            return True

        return self.to_dict() != other.to_dict()
