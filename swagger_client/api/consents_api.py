# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yodlee_client.api_client import ApiClient


class ConsentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_consent(self, consent_request, **kwargs):  # noqa: E501
        """Post Consent  # noqa: E501

        The generate consent service is used to generate all the consent information and permissions associated to a provider. <br/>The scope provided in the response is based on the providerId and the datasets provided in the input. <br/>If no dataset value is provided, the datasets that are configured for the customer will be considered. <br/>The configured dataset can be overridden by providing the dataset as an input. <br/>If no applicationName is provided in the input, the default applicationName will be considered. <b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_consent(consent_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateConsentRequest consent_request: Unique identifier for the provider site(mandatory), the name of the application,  <br/>the flag responsible to include html content in the response, <br/>when passed as true and the name of the dataset attribute supported by the provider. (required)
        :return: CreatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_consent_with_http_info(consent_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_consent_with_http_info(consent_request, **kwargs)  # noqa: E501
            return data

    def create_consent_with_http_info(self, consent_request, **kwargs):  # noqa: E501
        """Post Consent  # noqa: E501

        The generate consent service is used to generate all the consent information and permissions associated to a provider. <br/>The scope provided in the response is based on the providerId and the datasets provided in the input. <br/>If no dataset value is provided, the datasets that are configured for the customer will be considered. <br/>The configured dataset can be overridden by providing the dataset as an input. <br/>If no applicationName is provided in the input, the default applicationName will be considered. <b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_consent_with_http_info(consent_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateConsentRequest consent_request: Unique identifier for the provider site(mandatory), the name of the application,  <br/>the flag responsible to include html content in the response, <br/>when passed as true and the name of the dataset attribute supported by the provider. (required)
        :return: CreatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_consent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_request' is set
        if self.api_client.client_side_validation and ('consent_request' not in params or
                                                       params['consent_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `consent_request` when calling `create_consent`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'consent_request' in params:
            body_params = params['consent_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/consents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatedConsentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consent_details(self, consent_id, **kwargs):  # noqa: E501
        """Get Consent Details  # noqa: E501

        The get authorization URL for consent service provides the authorization URL for the renew consent flow, within the consent dashboard.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_details(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int consent_id: Consent Id generated through POST Consent. (required)
        :return: UpdatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_consent_details_with_http_info(consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_consent_details_with_http_info(consent_id, **kwargs)  # noqa: E501
            return data

    def get_consent_details_with_http_info(self, consent_id, **kwargs):  # noqa: E501
        """Get Consent Details  # noqa: E501

        The get authorization URL for consent service provides the authorization URL for the renew consent flow, within the consent dashboard.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consent_details_with_http_info(consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int consent_id: Consent Id generated through POST Consent. (required)
        :return: UpdatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consent_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_id' is set
        if self.api_client.client_side_validation and ('consent_id' not in params or
                                                       params['consent_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `consent_id` when calling `get_consent_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdatedConsentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consents(self, **kwargs):  # noqa: E501
        """Get Consents  # noqa: E501

        The get consent service is used to retrieve all the consents submitted to Yodlee. <br>The service can be used to build a manage consent interface or a consent dashboard to implement the renew and revoke consent flows.<br><b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_ids: Consent Id generated through POST Consent.
        :param str provider_account_ids: Unique identifier for the provider account resource. This is created during account addition.
        :return: ConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_consents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_consents_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_consents_with_http_info(self, **kwargs):  # noqa: E501
        """Get Consents  # noqa: E501

        The get consent service is used to retrieve all the consents submitted to Yodlee. <br>The service can be used to build a manage consent interface or a consent dashboard to implement the renew and revoke consent flows.<br><b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_ids: Consent Id generated through POST Consent.
        :param str provider_account_ids: Unique identifier for the provider account resource. This is created during account addition.
        :return: ConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_ids', 'provider_account_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consents" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'consent_ids' in params:
            query_params.append(('consentIds', params['consent_ids']))  # noqa: E501
        if 'provider_account_ids' in params:
            query_params.append(('providerAccountIds', params['provider_account_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/consents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConsentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_consent(self, consent_id, consent_request, **kwargs):  # noqa: E501
        """Put Consent  # noqa: E501

        The update consent service is used to capture the user acceptance of the consent presented to him or her. <br/>This service returns the authorization-redirect URL that should be used to display to the user, the bank's authentication interface.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_consent(consent_id, consent_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int consent_id: Consent Id generated through POST Consent. (required)
        :param UpdateConsentRequest consent_request: Applicable Open Banking data cluster values. (required)
        :return: UpdatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_consent_with_http_info(consent_id, consent_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_consent_with_http_info(consent_id, consent_request, **kwargs)  # noqa: E501
            return data

    def update_consent_with_http_info(self, consent_id, consent_request, **kwargs):  # noqa: E501
        """Put Consent  # noqa: E501

        The update consent service is used to capture the user acceptance of the consent presented to him or her. <br/>This service returns the authorization-redirect URL that should be used to display to the user, the bank's authentication interface.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_consent_with_http_info(consent_id, consent_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int consent_id: Consent Id generated through POST Consent. (required)
        :param UpdateConsentRequest consent_request: Applicable Open Banking data cluster values. (required)
        :return: UpdatedConsentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id', 'consent_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_consent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_id' is set
        if self.api_client.client_side_validation and ('consent_id' not in params or
                                                       params['consent_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `consent_id` when calling `update_consent`")  # noqa: E501
        # verify the required parameter 'consent_request' is set
        if self.api_client.client_side_validation and ('consent_request' not in params or
                                                       params['consent_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `consent_request` when calling `update_consent`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'consent_request' in params:
            body_params = params['consent_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdatedConsentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
