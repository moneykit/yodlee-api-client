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


class StatementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_statements(self, **kwargs):  # noqa: E501
        """Get Statements  # noqa: E501

        The statements service is used to get the list of statement related information. <br>By default, all the latest statements of active and to be closed accounts are retrieved for the user. <br>Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. <br>For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. <br>The default value of \"isLatest\" is true. To retrieve historical statements isLatest needs to be set to false.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_statements(async_req=True)
        >>> result = thread.get()

        :param account_id: accountId
        :type account_id: str
        :param container: creditCard/loan/insurance
        :type container: str
        :param from_date: from date for statement retrieval (YYYY-MM-DD)
        :type from_date: str
        :param is_latest: isLatest (true/false)
        :type is_latest: str
        :param status: ACTIVE,TO_BE_CLOSED,CLOSED
        :type status: str
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
        :rtype: StatementResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_statements_with_http_info(**kwargs)  # noqa: E501

    def get_statements_with_http_info(self, **kwargs):  # noqa: E501
        """Get Statements  # noqa: E501

        The statements service is used to get the list of statement related information. <br>By default, all the latest statements of active and to be closed accounts are retrieved for the user. <br>Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. <br>For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. <br>The default value of \"isLatest\" is true. To retrieve historical statements isLatest needs to be set to false.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_statements_with_http_info(async_req=True)
        >>> result = thread.get()

        :param account_id: accountId
        :type account_id: str
        :param container: creditCard/loan/insurance
        :type container: str
        :param from_date: from date for statement retrieval (YYYY-MM-DD)
        :type from_date: str
        :param is_latest: isLatest (true/false)
        :type is_latest: str
        :param status: ACTIVE,TO_BE_CLOSED,CLOSED
        :type status: str
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
        :rtype: tuple(StatementResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'account_id',
            'container',
            'from_date',
            'is_latest',
            'status'
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
                    " to method get_statements" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('account_id') is not None:  # noqa: E501
            query_params.append(('accountId', local_var_params['account_id']))  # noqa: E501
        if local_var_params.get('container') is not None:  # noqa: E501
            query_params.append(('container', local_var_params['container']))  # noqa: E501
        if local_var_params.get('from_date') is not None:  # noqa: E501
            query_params.append(('fromDate', local_var_params['from_date']))  # noqa: E501
        if local_var_params.get('is_latest') is not None:  # noqa: E501
            query_params.append(('isLatest', local_var_params['is_latest']))  # noqa: E501
        if local_var_params.get('status') is not None:  # noqa: E501
            query_params.append(('status', local_var_params['status']))  # noqa: E501

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
            200: "StatementResponse",
            400: "YodleeError",
            401: None,
            404: None,
        }

        return self.api_client.call_api(
            '/statements', 'GET',
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
