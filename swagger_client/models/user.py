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


class User(object):
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
        'preferences': 'UserResponsePreferences',
        'session': 'UserSession',
        'login_name': 'str',
        'name': 'Name',
        'id': 'int',
        'role_type': 'str'
    }

    attribute_map = {
        'preferences': 'preferences',
        'session': 'session',
        'login_name': 'loginName',
        'name': 'name',
        'id': 'id',
        'role_type': 'roleType'
    }

    def __init__(self, preferences=None, session=None, login_name=None, name=None, id=None, role_type=None, _configuration=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._preferences = None
        self._session = None
        self._login_name = None
        self._name = None
        self._id = None
        self._role_type = None
        self.discriminator = None

        if preferences is not None:
            self.preferences = preferences
        if session is not None:
            self.session = session
        if login_name is not None:
            self.login_name = login_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if role_type is not None:
            self.role_type = role_type

    @property
    def preferences(self):
        """Gets the preferences of this User.  # noqa: E501

        Preferences of the user to be respected in the data provided through various API services.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :return: The preferences of this User.  # noqa: E501
        :rtype: UserResponsePreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this User.

        Preferences of the user to be respected in the data provided through various API services.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :param preferences: The preferences of this User.  # noqa: E501
        :type: UserResponsePreferences
        """

        self._preferences = preferences

    @property
    def session(self):
        """Gets the session of this User.  # noqa: E501

        Session token of the user using which other services are invoked in the system.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li></ul>  # noqa: E501

        :return: The session of this User.  # noqa: E501
        :rtype: UserSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this User.

        Session token of the user using which other services are invoked in the system.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li></ul>  # noqa: E501

        :param session: The session of this User.  # noqa: E501
        :type: UserSession
        """

        self._session = session

    @property
    def login_name(self):
        """Gets the login_name of this User.  # noqa: E501

        The login name of the user used for authentication.<br><br><b>Endpoints</b>:<ul><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :return: The login_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this User.

        The login name of the user used for authentication.<br><br><b>Endpoints</b>:<ul><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :param login_name: The login_name of this User.  # noqa: E501
        :type: str
        """

        self._login_name = login_name

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501

        First, middle and last names of the user.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :return: The name of this User.  # noqa: E501
        :rtype: Name
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.

        First, middle and last names of the user.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :param name: The name of this User.  # noqa: E501
        :type: Name
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        The unique identifier of a consumer/user in Yodlee system for whom the API services would be accessed for.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        The unique identifier of a consumer/user in Yodlee system for whom the API services would be accessed for.<br><br><b>Endpoints</b>:<ul><li>POST user/samlLogin</li><li>POST user/register</li><li>GET user</li></ul>  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def role_type(self):
        """Gets the role_type of this User.  # noqa: E501


        :return: The role_type of this User.  # noqa: E501
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        """Sets the role_type of this User.


        :param role_type: The role_type of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["INDIVIDUAL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                role_type not in allowed_values):
            raise ValueError(
                "Invalid value for `role_type` ({0}), must be one of {1}"  # noqa: E501
                .format(role_type, allowed_values)
            )

        self._role_type = role_type

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
