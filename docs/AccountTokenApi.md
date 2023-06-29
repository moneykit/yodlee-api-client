# yodlee.AccountTokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_payment_processor_token**](AccountTokenApi.md#generate_payment_processor_token) | **POST** /paymentProcessor/token | Create Account Token
[**revoke_payment_processor_token**](AccountTokenApi.md#revoke_payment_processor_token) | **DELETE** /paymentProcessor/token | Delete Account Token


# **generate_payment_processor_token**
> PaymentProcessorTokenResponse generate_payment_processor_token(token_request)

Create Account Token

The create account token service allows you to create a secure <code>processorToken</code> for a user's verified financial account. This <code>processorToken</code> can then be shared with one of our payment processor partners.

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
    api_instance = yodlee.AccountTokenApi(api_client)
    token_request = yodlee.PaymentProcessorTokenRequest() # PaymentProcessorTokenRequest | account information

    try:
        # Create Account Token
        api_response = api_instance.generate_payment_processor_token(token_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountTokenApi->generate_payment_processor_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**PaymentProcessorTokenRequest**](PaymentProcessorTokenRequest.md)| account information | 

### Return type

[**PaymentProcessorTokenResponse**](PaymentProcessorTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y007 : Authorization header missing&lt;br&gt;Y008 : Invalid token in authorization header&lt;br&gt;Y833 : Invalid values(s) for accountId&lt;br&gt;Y800 : Invalid value for processor&lt;br&gt;Y813 : accountId should be provided&lt;br&gt;Y813 : processor should be provided |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_payment_processor_token**
> revoke_payment_processor_token(processor_token)

Delete Account Token

The delete account token service allows you to revoke a previously generated <code>processorToken</code>. It is recommended to use this service when you want to disallow further access to the user's financial account, for instance when a user removes their account from your application.

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
    api_instance = yodlee.AccountTokenApi(api_client)
    processor_token = 'processor_token_example' # str | The token that you want to delete.

    try:
        # Delete Account Token
        api_instance.revoke_payment_processor_token(processor_token)
    except ApiException as e:
        print("Exception when calling AccountTokenApi->revoke_payment_processor_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token** | **str**| The token that you want to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Y007 : Authorization header missing&lt;br&gt;Y008 : Invalid token in authorization header&lt;br&gt;Y016 : processorToken header missing |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

