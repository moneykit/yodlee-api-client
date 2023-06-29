# yodlee.VerifyAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiate_account_verification**](VerifyAccountApi.md#initiate_account_verification) | **POST** /verifyAccount/{providerAccountId} | Verify Accounts Using Transactions


# **initiate_account_verification**
> VerifyAccountResponse initiate_account_verification(provider_account_id, verification_param)

Verify Accounts Using Transactions

The verify account service is used to verify the account's ownership by  matching the transaction details with the accounts aggregated for the user.<br><ul><li>If a match is identified, the service returns details of all the accounts along with the matched transaction's details.<li>If no transaction match is found, an empty response will be returned.<li>A maximum of 5 transactionCriteria can be passed in a request.<li>The baseType, date, and amount parameters should mandatorily be passed.<li>The optional dateVariance parameter cannot be more than 7 days. For example, +7, -4, or +/-2.<li>Pass the container or accountId parameters for better performance.<li>This service supports the localization feature and accepts locale as a header parameter.</li></ul>

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
    api_instance = yodlee.VerifyAccountApi(api_client)
    provider_account_id = 'provider_account_id_example' # str | providerAccountId
verification_param = yodlee.VerifyAccountRequest() # VerifyAccountRequest | verificationParam

    try:
        # Verify Accounts Using Transactions
        api_response = api_instance.initiate_account_verification(provider_account_id, verification_param)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VerifyAccountApi->initiate_account_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_account_id** | **str**| providerAccountId | 
 **verification_param** | [**VerifyAccountRequest**](VerifyAccountRequest.md)| verificationParam | 

### Return type

[**VerifyAccountResponse**](VerifyAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for container&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for amount&lt;br&gt;Y800 : Invalid value for dateVariance&lt;br&gt;Y801 : Invalid length for keyword&lt;br&gt;Y804 : Permitted values of dateVariance between 1 - 7&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y807 : Resource not found&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y812 : Required field/value - transactionCriteria missing in the input&lt;br&gt;Y812 : Required field/value - amount missing in the transactionCriteria&lt;br&gt;Y812 : Required field/value - amount date in the transactionCriteria&lt;br&gt;Y812 : Required field/value - baseType missing in the transactionCriteria&lt;br&gt;Y823 : Transaction not applicable for container &lt;br&gt;Y824 : The maximum number of transactionCriteria permitted is 5&lt;br&gt;Y857 : Transactions are not refreshed in the past 24 hours&lt;br&gt;Y858 : Only active accounts can be verified&lt;br&gt;Y901 : Service not supported&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

