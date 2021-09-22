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


class DataExtractsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_data_extracts_events(self, event_name, from_date, to_date, **kwargs):  # noqa: E501
        """Get Events  # noqa: E501

        The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.<br>Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page.<br>You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today's date.<br>This service is only invoked with either admin access token or a cobrand session.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_extracts_events(event_name, from_date, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_name: Event Name (required)
        :param str from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :param str to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :return: DataExtractsEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_data_extracts_events_with_http_info(event_name, from_date, to_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_extracts_events_with_http_info(event_name, from_date, to_date, **kwargs)  # noqa: E501
            return data

    def get_data_extracts_events_with_http_info(self, event_name, from_date, to_date, **kwargs):  # noqa: E501
        """Get Events  # noqa: E501

        The get extracts events service is used to learn about occurrences of data extract related events. This service currently supports only the DATA_UPDATES event.<br>Passing the event name as DATA_UPDATES provides information about users for whom data has been modified in the system for the specified time range. To learn more, please refer to the <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page.<br>You can retrieve data in increments of no more than 60 minutes over the period of the last 7 days from today's date.<br>This service is only invoked with either admin access token or a cobrand session.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_extracts_events_with_http_info(event_name, from_date, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_name: Event Name (required)
        :param str from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :param str to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :return: DataExtractsEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_name', 'from_date', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_extracts_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_name' is set
        if self.api_client.client_side_validation and ('event_name' not in params or
                                                       params['event_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `event_name` when calling `get_data_extracts_events`")  # noqa: E501
        # verify the required parameter 'from_date' is set
        if self.api_client.client_side_validation and ('from_date' not in params or
                                                       params['from_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `from_date` when calling `get_data_extracts_events`")  # noqa: E501
        # verify the required parameter 'to_date' is set
        if self.api_client.client_side_validation and ('to_date' not in params or
                                                       params['to_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `to_date` when calling `get_data_extracts_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'event_name' in params:
            query_params.append(('eventName', params['event_name']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

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
            '/dataExtracts/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataExtractsEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_data_extracts_user_data(self, from_date, login_name, to_date, **kwargs):  # noqa: E501
        """Get userData  # noqa: E501

        The get user data service is used to get a user's modified data for a particular period of time for accounts, transactions, holdings, and provider account information.<br>The time difference between fromDate and toDate fields cannot be more than 60 minutes.<br>By default, pagination is available for the transaction entity in this API. In the first response, the API will retrieve 500 transactions along with other data. The response header will provide a link to retrieve the next set of transactions.<br>In the response body of the first API response, totalTransactionsCount indicates the total number of transactions the API will retrieve for the user.<br>This service is only invoked with either admin access token or a cobrand session.<br/>Refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page for more information.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_extracts_user_data(from_date, login_name, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :param str login_name: Login Name (required)
        :param str to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :return: DataExtractsUserDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_data_extracts_user_data_with_http_info(from_date, login_name, to_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_extracts_user_data_with_http_info(from_date, login_name, to_date, **kwargs)  # noqa: E501
            return data

    def get_data_extracts_user_data_with_http_info(self, from_date, login_name, to_date, **kwargs):  # noqa: E501
        """Get userData  # noqa: E501

        The get user data service is used to get a user's modified data for a particular period of time for accounts, transactions, holdings, and provider account information.<br>The time difference between fromDate and toDate fields cannot be more than 60 minutes.<br>By default, pagination is available for the transaction entity in this API. In the first response, the API will retrieve 500 transactions along with other data. The response header will provide a link to retrieve the next set of transactions.<br>In the response body of the first API response, totalTransactionsCount indicates the total number of transactions the API will retrieve for the user.<br>This service is only invoked with either admin access token or a cobrand session.<br/>Refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/DataExtracts\">dataExtracts</a> page for more information.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_extracts_user_data_with_http_info(from_date, login_name, to_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str from_date: From DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :param str login_name: Login Name (required)
        :param str to_date: To DateTime (YYYY-MM-DDThh:mm:ssZ) (required)
        :return: DataExtractsUserDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['from_date', 'login_name', 'to_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_extracts_user_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'from_date' is set
        if self.api_client.client_side_validation and ('from_date' not in params or
                                                       params['from_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `from_date` when calling `get_data_extracts_user_data`")  # noqa: E501
        # verify the required parameter 'login_name' is set
        if self.api_client.client_side_validation and ('login_name' not in params or
                                                       params['login_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `login_name` when calling `get_data_extracts_user_data`")  # noqa: E501
        # verify the required parameter 'to_date' is set
        if self.api_client.client_side_validation and ('to_date' not in params or
                                                       params['to_date'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `to_date` when calling `get_data_extracts_user_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'login_name' in params:
            query_params.append(('loginName', params['login_name']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501

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
            '/dataExtracts/userData', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataExtractsUserDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
