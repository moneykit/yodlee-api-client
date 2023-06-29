# yodlee.StatementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statements**](StatementsApi.md#get_statements) | **GET** /statements | Get Statements


# **get_statements**
> StatementResponse get_statements(account_id=account_id, container=container, from_date=from_date, is_latest=is_latest, status=status)

Get Statements

The statements service is used to get the list of statement related information. <br>By default, all the latest statements of active and to be closed accounts are retrieved for the user. <br>Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. <br>For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. <br>The default value of \"isLatest\" is true. To retrieve historical statements isLatest needs to be set to false.<br>

### Example

```python
from __future__ import print_function
import time
import yodlee
from yodlee.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yodlee.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with yodlee.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = yodlee.StatementsApi(api_client)
    account_id = 'account_id_example' # str | accountId (optional)
container = 'container_example' # str | creditCard/loan/insurance (optional)
from_date = 'from_date_example' # str | from date for statement retrieval (YYYY-MM-DD) (optional)
is_latest = 'is_latest_example' # str | isLatest (true/false) (optional)
status = 'status_example' # str | ACTIVE,TO_BE_CLOSED,CLOSED (optional)

    try:
        # Get Statements
        api_response = api_instance.get_statements(account_id=account_id, container=container, from_date=from_date, is_latest=is_latest, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatementsApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | [optional] 
 **container** | **str**| creditCard/loan/insurance | [optional] 
 **from_date** | **str**| from date for statement retrieval (YYYY-MM-DD) | [optional] 
 **is_latest** | **str**| isLatest (true/false) | [optional] 
 **status** | **str**| ACTIVE,TO_BE_CLOSED,CLOSED | [optional] 

### Return type

[**StatementResponse**](StatementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for status&lt;br&gt;Y805 : Multiple containers not supported&lt;br&gt;Y800 : Invalid value for container&lt;br&gt;Y800 : Invalid value for isLatest&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

