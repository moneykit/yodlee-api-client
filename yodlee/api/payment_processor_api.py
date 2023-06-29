# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yodlee.api_client import ApiClient
from yodlee.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PaymentProcessorApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_verified_account(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Details  # noqa: E501

        The get account details service retrieves account information such as account name, type, status, balance, account number and transfer code (for example, routing number of the bank account in the US) of the verified account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for details related to the financial account, for instance, the full account number and bank transfer code for initiating a payment.<br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaymentAccountResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_verified_account_with_http_info(processor_token, **kwargs)  # noqa: E501

    def get_verified_account_with_http_info(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Details  # noqa: E501

        The get account details service retrieves account information such as account name, type, status, balance, account number and transfer code (for example, routing number of the bank account in the US) of the verified account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for details related to the financial account, for instance, the full account number and bank transfer code for initiating a payment.<br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account_with_http_info(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaymentAccountResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'processor_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_verified_account" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'processor_token' is set
        if self.api_client.client_side_validation and local_var_params.get('processor_token') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `processor_token` when calling `get_verified_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'processor_token' in local_var_params:
            header_params['processorToken'] = local_var_params['processor_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "PaymentAccountResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/partner/paymentProcessor/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_verified_account_balance(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Balance  # noqa: E501

        The get account balance service retrieves the account balance information of the verified account associated with the <code>processorToken</code>. The response returns additional account information including account names, type and status, along with the account balance information. <br>This service forces an update of the account balances. While other services also return the account balances, this service attempts to refresh the account balances in real-time rather than return a cached value. Refer to the <code>lastUpdated</code> field to determine when the account balances were refreshed. We recommend using this service when looking for the latest balance for the account.<br>While posting a debit against an account, it is generally advisable to check the available balance field to verify the availability of sufficient funds. This service returns both available and current balances: <ul><li><b>Available Balance</b> is the amount in the account that is available for spending. The value is aggregated from the FI. For checking accounts with overdrafts, the available balance amount may include the overdraft amount if the FI adds the overdraft balance to the available balance.</li><li><b>Current Balance</b> is the total amount of money in the account, aggregated from the FI.</li></ul><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account_balance(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaymentAccountBalanceResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_verified_account_balance_with_http_info(processor_token, **kwargs)  # noqa: E501

    def get_verified_account_balance_with_http_info(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Balance  # noqa: E501

        The get account balance service retrieves the account balance information of the verified account associated with the <code>processorToken</code>. The response returns additional account information including account names, type and status, along with the account balance information. <br>This service forces an update of the account balances. While other services also return the account balances, this service attempts to refresh the account balances in real-time rather than return a cached value. Refer to the <code>lastUpdated</code> field to determine when the account balances were refreshed. We recommend using this service when looking for the latest balance for the account.<br>While posting a debit against an account, it is generally advisable to check the available balance field to verify the availability of sufficient funds. This service returns both available and current balances: <ul><li><b>Available Balance</b> is the amount in the account that is available for spending. The value is aggregated from the FI. For checking accounts with overdrafts, the available balance amount may include the overdraft amount if the FI adds the overdraft balance to the available balance.</li><li><b>Current Balance</b> is the total amount of money in the account, aggregated from the FI.</li></ul><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account_balance_with_http_info(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaymentAccountBalanceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'processor_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_verified_account_balance" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'processor_token' is set
        if self.api_client.client_side_validation and local_var_params.get('processor_token') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `processor_token` when calling `get_verified_account_balance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'processor_token' in local_var_params:
            header_params['processorToken'] = local_var_params['processor_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "PaymentAccountBalanceResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/partner/paymentProcessor/account/balance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_verified_account_holder(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Holder Details  # noqa: E501

        The get account holder details service retrieves the account holder information such as name, email, phone number, address, etc. of the verified financial account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for information related to the account holder(s), for instance, to confirm the account holder's name. <br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account_holder(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PaymentAccountHolderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_verified_account_holder_with_http_info(processor_token, **kwargs)  # noqa: E501

    def get_verified_account_holder_with_http_info(self, processor_token, **kwargs):  # noqa: E501
        """Get Account Holder Details  # noqa: E501

        The get account holder details service retrieves the account holder information such as name, email, phone number, address, etc. of the verified financial account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for information related to the account holder(s), for instance, to confirm the account holder's name. <br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_verified_account_holder_with_http_info(processor_token, async_req=True)
        >>> result = thread.get()

        :param processor_token: Token shared by customer to access financial account information. (required)
        :type processor_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PaymentAccountHolderResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'processor_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_verified_account_holder" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'processor_token' is set
        if self.api_client.client_side_validation and local_var_params.get('processor_token') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `processor_token` when calling `get_verified_account_holder`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'processor_token' in local_var_params:
            header_params['processorToken'] = local_var_params['processor_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "PaymentAccountHolderResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/partner/paymentProcessor/account/holder', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))