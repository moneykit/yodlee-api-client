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


class DerivedApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_holding_summary(self, **kwargs):  # noqa: E501
        """Get Holding Summary  # noqa: E501

        The get holding summary service is used to get the summary of asset classifications for the user.<br>By default, accounts with status as ACTIVE and TO BE CLOSED will be considered.<br>If the include parameter value is passed as details then a summary with holdings and account information is returned.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_holding_summary(async_req=True)
        >>> result = thread.get()

        :param account_ids: Comma separated accountIds
        :type account_ids: str
        :param classification_type: e.g. Country, Sector, etc.
        :type classification_type: str
        :param include: details
        :type include: str
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
        :rtype: DerivedHoldingSummaryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_holding_summary_with_http_info(**kwargs)  # noqa: E501

    def get_holding_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get Holding Summary  # noqa: E501

        The get holding summary service is used to get the summary of asset classifications for the user.<br>By default, accounts with status as ACTIVE and TO BE CLOSED will be considered.<br>If the include parameter value is passed as details then a summary with holdings and account information is returned.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_holding_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param account_ids: Comma separated accountIds
        :type account_ids: str
        :param classification_type: e.g. Country, Sector, etc.
        :type classification_type: str
        :param include: details
        :type include: str
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
        :rtype: tuple(DerivedHoldingSummaryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'account_ids',
            'classification_type',
            'include'
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
                    " to method get_holding_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('account_ids') is not None:  # noqa: E501
            query_params.append(('accountIds', local_var_params['account_ids']))  # noqa: E501
        if local_var_params.get('classification_type') is not None:  # noqa: E501
            query_params.append(('classificationType', local_var_params['classification_type']))  # noqa: E501
        if local_var_params.get('include') is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "DerivedHoldingSummaryResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/derived/holdingSummary', 'GET',
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

    def get_networth(self, **kwargs):  # noqa: E501
        """Get Networth Summary  # noqa: E501

        The get networth service is used to get the networth for the user.<br>If the include parameter value is passed as details then networth with historical balances is returned. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_networth(async_req=True)
        >>> result = thread.get()

        :param account_ids: comma separated accountIds
        :type account_ids: str
        :param container: bank/creditCard/investment/insurance/loan/realEstate/otherAssets/otherLiabilities
        :type container: str
        :param from_date: from date for balance retrieval (YYYY-MM-DD)
        :type from_date: str
        :param include: details
        :type include: str
        :param interval: D-daily, W-weekly or M-monthly
        :type interval: str
        :param skip: skip (Min 0)
        :type skip: int
        :param to_date: toDate for balance retrieval (YYYY-MM-DD)
        :type to_date: str
        :param top: top (Max 500)
        :type top: int
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
        :rtype: DerivedNetworthResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_networth_with_http_info(**kwargs)  # noqa: E501

    def get_networth_with_http_info(self, **kwargs):  # noqa: E501
        """Get Networth Summary  # noqa: E501

        The get networth service is used to get the networth for the user.<br>If the include parameter value is passed as details then networth with historical balances is returned. <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_networth_with_http_info(async_req=True)
        >>> result = thread.get()

        :param account_ids: comma separated accountIds
        :type account_ids: str
        :param container: bank/creditCard/investment/insurance/loan/realEstate/otherAssets/otherLiabilities
        :type container: str
        :param from_date: from date for balance retrieval (YYYY-MM-DD)
        :type from_date: str
        :param include: details
        :type include: str
        :param interval: D-daily, W-weekly or M-monthly
        :type interval: str
        :param skip: skip (Min 0)
        :type skip: int
        :param to_date: toDate for balance retrieval (YYYY-MM-DD)
        :type to_date: str
        :param top: top (Max 500)
        :type top: int
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
        :rtype: tuple(DerivedNetworthResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'account_ids',
            'container',
            'from_date',
            'include',
            'interval',
            'skip',
            'to_date',
            'top'
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
                    " to method get_networth" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('account_ids') is not None:  # noqa: E501
            query_params.append(('accountIds', local_var_params['account_ids']))  # noqa: E501
        if local_var_params.get('container') is not None:  # noqa: E501
            query_params.append(('container', local_var_params['container']))  # noqa: E501
        if local_var_params.get('from_date') is not None:  # noqa: E501
            query_params.append(('fromDate', local_var_params['from_date']))  # noqa: E501
        if local_var_params.get('include') is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
        if local_var_params.get('interval') is not None:  # noqa: E501
            query_params.append(('interval', local_var_params['interval']))  # noqa: E501
        if local_var_params.get('skip') is not None:  # noqa: E501
            query_params.append(('skip', local_var_params['skip']))  # noqa: E501
        if local_var_params.get('to_date') is not None:  # noqa: E501
            query_params.append(('toDate', local_var_params['to_date']))  # noqa: E501
        if local_var_params.get('top') is not None:  # noqa: E501
            query_params.append(('top', local_var_params['top']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "DerivedNetworthResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/derived/networth', 'GET',
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

    def get_transaction_summary(self, group_by, **kwargs):  # noqa: E501
        """Get Transaction Summary  # noqa: E501

        The transaction summary service provides the summary values of transactions for the given date range by category type, high-level categories, or system-defined categories.<br><br>Yodlee has the transaction data stored for a day, month, year and week per category as per the availability of user's data. If the include parameter value is passed as details, then summary details will be returned depending on the interval passed-monthly is the default.<br><br><b>Notes:</b><ol> <li> Details can be requested for only one system-defined category<li>Passing categoryType is mandatory except when the groupBy value is CATEGORY_TYPE<li>Dates will not be respected for monthly, yearly, and weekly details<li>When monthly details are requested, only the fromDate and toDate month will be respected<li>When yearly details are requested, only the fromDate and toDate year will be respected<li>For weekly data points, details will be provided for every Sunday date available within the fromDate and toDate<li>This service supports the localization feature and accepts locale as a header parameter</li></ol>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_summary(group_by, async_req=True)
        >>> result = thread.get()

        :param group_by: CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY (required)
        :type group_by: str
        :param account_id: comma separated account Ids
        :type account_id: str
        :param category_id: comma separated categoryIds
        :type category_id: str
        :param category_type: INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION
        :type category_type: str
        :param from_date: YYYY-MM-DD format
        :type from_date: str
        :param include: details
        :type include: str
        :param include_user_category: TRUE/FALSE
        :type include_user_category: bool
        :param interval: D-daily, W-weekly, M-mothly or Y-yearly
        :type interval: str
        :param to_date: YYYY-MM-DD format
        :type to_date: str
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
        :rtype: DerivedTransactionSummaryResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_summary_with_http_info(group_by, **kwargs)  # noqa: E501

    def get_transaction_summary_with_http_info(self, group_by, **kwargs):  # noqa: E501
        """Get Transaction Summary  # noqa: E501

        The transaction summary service provides the summary values of transactions for the given date range by category type, high-level categories, or system-defined categories.<br><br>Yodlee has the transaction data stored for a day, month, year and week per category as per the availability of user's data. If the include parameter value is passed as details, then summary details will be returned depending on the interval passed-monthly is the default.<br><br><b>Notes:</b><ol> <li> Details can be requested for only one system-defined category<li>Passing categoryType is mandatory except when the groupBy value is CATEGORY_TYPE<li>Dates will not be respected for monthly, yearly, and weekly details<li>When monthly details are requested, only the fromDate and toDate month will be respected<li>When yearly details are requested, only the fromDate and toDate year will be respected<li>For weekly data points, details will be provided for every Sunday date available within the fromDate and toDate<li>This service supports the localization feature and accepts locale as a header parameter</li></ol>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_summary_with_http_info(group_by, async_req=True)
        >>> result = thread.get()

        :param group_by: CATEGORY_TYPE, HIGH_LEVEL_CATEGORY or CATEGORY (required)
        :type group_by: str
        :param account_id: comma separated account Ids
        :type account_id: str
        :param category_id: comma separated categoryIds
        :type category_id: str
        :param category_type: INCOME, EXPENSE, TRANSFER, UNCATEGORIZE or DEFERRED_COMPENSATION
        :type category_type: str
        :param from_date: YYYY-MM-DD format
        :type from_date: str
        :param include: details
        :type include: str
        :param include_user_category: TRUE/FALSE
        :type include_user_category: bool
        :param interval: D-daily, W-weekly, M-mothly or Y-yearly
        :type interval: str
        :param to_date: YYYY-MM-DD format
        :type to_date: str
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
        :rtype: tuple(DerivedTransactionSummaryResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'group_by',
            'account_id',
            'category_id',
            'category_type',
            'from_date',
            'include',
            'include_user_category',
            'interval',
            'to_date'
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
                    " to method get_transaction_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'group_by' is set
        if self.api_client.client_side_validation and local_var_params.get('group_by') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `group_by` when calling `get_transaction_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('account_id') is not None:  # noqa: E501
            query_params.append(('accountId', local_var_params['account_id']))  # noqa: E501
        if local_var_params.get('category_id') is not None:  # noqa: E501
            query_params.append(('categoryId', local_var_params['category_id']))  # noqa: E501
        if local_var_params.get('category_type') is not None:  # noqa: E501
            query_params.append(('categoryType', local_var_params['category_type']))  # noqa: E501
        if local_var_params.get('from_date') is not None:  # noqa: E501
            query_params.append(('fromDate', local_var_params['from_date']))  # noqa: E501
        if local_var_params.get('group_by') is not None:  # noqa: E501
            query_params.append(('groupBy', local_var_params['group_by']))  # noqa: E501
        if local_var_params.get('include') is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
        if local_var_params.get('include_user_category') is not None:  # noqa: E501
            query_params.append(('includeUserCategory', local_var_params['include_user_category']))  # noqa: E501
        if local_var_params.get('interval') is not None:  # noqa: E501
            query_params.append(('interval', local_var_params['interval']))  # noqa: E501
        if local_var_params.get('to_date') is not None:  # noqa: E501
            query_params.append(('toDate', local_var_params['to_date']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "DerivedTransactionSummaryResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/derived/transactionSummary', 'GET',
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
