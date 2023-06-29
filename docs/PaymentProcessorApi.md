# yodlee.PaymentProcessorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_verified_account**](PaymentProcessorApi.md#get_verified_account) | **GET** /partner/paymentProcessor/account | Get Account Details
[**get_verified_account_balance**](PaymentProcessorApi.md#get_verified_account_balance) | **GET** /partner/paymentProcessor/account/balance | Get Account Balance
[**get_verified_account_holder**](PaymentProcessorApi.md#get_verified_account_holder) | **GET** /partner/paymentProcessor/account/holder | Get Account Holder Details


# **get_verified_account**
> PaymentAccountResponse get_verified_account(processor_token)

Get Account Details

The get account details service retrieves account information such as account name, type, status, balance, account number and transfer code (for example, routing number of the bank account in the US) of the verified account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for details related to the financial account, for instance, the full account number and bank transfer code for initiating a payment.<br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.

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
    api_instance = yodlee.PaymentProcessorApi(api_client)
    processor_token = 'processor_token_example' # str | Token shared by customer to access financial account information.

    try:
        # Get Account Details
        api_response = api_instance.get_verified_account(processor_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentProcessorApi->get_verified_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token** | **str**| Token shared by customer to access financial account information. | 

### Return type

[**PaymentAccountResponse**](PaymentAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y007 : Authorization header missing&lt;br&gt;Y008 : Invalid token in authorization header&lt;br&gt;Y800 : Invalid value for processorToken&lt;br&gt;Y016 : processorToken header missing |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verified_account_balance**
> PaymentAccountBalanceResponse get_verified_account_balance(processor_token)

Get Account Balance

The get account balance service retrieves the account balance information of the verified account associated with the <code>processorToken</code>. The response returns additional account information including account names, type and status, along with the account balance information. <br>This service forces an update of the account balances. While other services also return the account balances, this service attempts to refresh the account balances in real-time rather than return a cached value. Refer to the <code>lastUpdated</code> field to determine when the account balances were refreshed. We recommend using this service when looking for the latest balance for the account.<br>While posting a debit against an account, it is generally advisable to check the available balance field to verify the availability of sufficient funds. This service returns both available and current balances: <ul><li><b>Available Balance</b> is the amount in the account that is available for spending. The value is aggregated from the FI. For checking accounts with overdrafts, the available balance amount may include the overdraft amount if the FI adds the overdraft balance to the available balance.</li><li><b>Current Balance</b> is the total amount of money in the account, aggregated from the FI.</li></ul><br><b>Note: </b>Remember to include the <code>Authorization</code> header.

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
    api_instance = yodlee.PaymentProcessorApi(api_client)
    processor_token = 'processor_token_example' # str | Token shared by customer to access financial account information.

    try:
        # Get Account Balance
        api_response = api_instance.get_verified_account_balance(processor_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentProcessorApi->get_verified_account_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token** | **str**| Token shared by customer to access financial account information. | 

### Return type

[**PaymentAccountBalanceResponse**](PaymentAccountBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y007 : Authorization header missing&lt;br&gt;Y008 : Invalid token in authorization header&lt;br&gt;Y800 : Invalid value for processorToken&lt;br&gt;Y016 : processorToken header missing |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verified_account_holder**
> PaymentAccountHolderResponse get_verified_account_holder(processor_token)

Get Account Holder Details

The get account holder details service retrieves the account holder information such as name, email, phone number, address, etc. of the verified financial account associated with the <code>processorToken</code>. The <code>lastUpdated</code> field indicates when the account information was last updated. We recommend using this service when looking for information related to the account holder(s), for instance, to confirm the account holder's name. <br><br><b>Note: </b>Remember to include the <code>Authorization</code> header.

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
    api_instance = yodlee.PaymentProcessorApi(api_client)
    processor_token = 'processor_token_example' # str | Token shared by customer to access financial account information.

    try:
        # Get Account Holder Details
        api_response = api_instance.get_verified_account_holder(processor_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentProcessorApi->get_verified_account_holder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_token** | **str**| Token shared by customer to access financial account information. | 

### Return type

[**PaymentAccountHolderResponse**](PaymentAccountHolderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y007 : Authorization header missing&lt;br&gt;Y008 : Invalid token in authorization header&lt;br&gt;Y800 : Invalid value for processorToken&lt;br&gt;Y016 : processorToken header missing |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

