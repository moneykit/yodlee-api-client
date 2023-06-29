# yodlee.ProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_providers**](ProvidersApi.md#get_all_providers) | **GET** /providers | Get Providers
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /providers/{providerId} | Get Provider Details
[**get_providers_count**](ProvidersApi.md#get_providers_count) | **GET** /providers/count | Get Providers Count


# **get_all_providers**
> ProviderResponse get_all_providers(capability=capability, datasetfilter=datasetfilter, full_account_number_fields=full_account_number_fields, institution_id=institution_id, name=name, priority=priority, provider_id=provider_id, skip=skip, top=top)

Get Providers

The get provider service is used to get all the providers that are enabled, search a provider service by name or routing number and get popular sites of a region. <br>Searching for a provider using a routing number is applicable only to the USA and Canada regions.<br>The valid values for priority are: <br>   1. cobrand: Returns providers enabled for the cobrand (Default priority)<br>   2. popular: Returns providers popular among users of the customer<br><br>Only the datasets, attributes, and containers that are enabled for the customer will be returned in the response.<br>Input for the dataset$filter should adhere to the following expression:<br><dataset.name>[<attribute.name>.container[<container> OR <container>] OR <attribute.name>.container[<container>]] <br>OR <dataset.name>[<attribute.name> OR <attribute.name>]<br><b>dataset$filter value examples:</b><br>ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank OR investment OR creditCard]]<br>ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]<br>BASIC_AGG_DATA[ACCOUNT_DETAILS.container[bank OR investment] OR HOLDINGS.container[bank]] OR ACCT_PROFILE[FULL_ACCT_NUMBER.container[bank]]<br>BASIC_AGG_DATA<br>BASIC_AGG_DATA OR ACCT_PROFILE<br>BASIC_AGG_DATA [ ACCOUNT_DETAILS OR HOLDINGS ]<br>BASIC_AGG_DATA [ ACCOUNT_DETAILS] OR DOCUMENT <br>BASIC_AGG_DATA [ BASIC_ACCOUNT_INFO OR ACCOUNT_DETAILS ] <br><br>The fullAcountNumberFields is specified to filter the providers that have paymentAccountNumber or unmaskedAccountNumber support in the FULL_ACCT_NUMBER dataset attribute.<br><b>Examples for usage of fullAccountNumberFields </b><br>dataset$filter=ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp; fullAccountNumberFields=paymentAccountNumber<br>dataset$filter=ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp; fullAccountNumberFields=unmaskedAccountNumber<br>dataset$filter=ACCT_PROFILE[ FULL_ACCT_NUMBER.container [ bank ]] &amp; fullAccountNumberFields=unmaskedAccountNumber,paymentAccountNumber<br><br>The skip and top parameters are used for pagination. In the skip and top parameters, pass the number of records to be skipped and retrieved, respectively.<br>The response header provides the links to retrieve the next and previous set of transactions.<br><br><b>Note:</b> <ol><li>In a product flow involving user interaction, Yodlee recommends invoking this service with filters.<li>Without filters, the service may perform slowly as it takes a few minutes to return data in the response.<li>The AuthParameter appears in the response only in case of token-based aggregation sites.<li>The pagination feature only applies when the priority parameter is set as cobrand. If no values are provided in the skip and top parameters, the API will only return the first 500 records.<li>This service supports the localization feature and accepts locale as a header parameter.<li>The capability has been deprecated in query parameter and response.</li></ol>

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
    api_instance = yodlee.ProvidersApi(api_client)
    capability = 'capability_example' # str | CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated (optional)
datasetfilter = 'datasetfilter_example' # str | Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. (optional)
full_account_number_fields = 'full_account_number_fields_example' # str | Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. (optional)
institution_id = 56 # int | Institution Id for Single site selection (optional)
name = 'name_example' # str | Name in minimum 1 character or routing number. (optional)
priority = 'priority_example' # str | Search priority (optional)
provider_id = 'provider_id_example' # str | Max 5 Comma seperated Provider Ids (optional)
skip = 56 # int | skip (Min 0) - This is not applicable along with 'name' parameter. (optional)
top = 56 # int | top (Max 500) - This is not applicable along with 'name' parameter. (optional)

    try:
        # Get Providers
        api_response = api_instance.get_all_providers(capability=capability, datasetfilter=datasetfilter, full_account_number_fields=full_account_number_fields, institution_id=institution_id, name=name, priority=priority, provider_id=provider_id, skip=skip, top=top)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->get_all_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capability** | **str**| CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated | [optional] 
 **datasetfilter** | **str**| Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. | [optional] 
 **full_account_number_fields** | **str**| Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. | [optional] 
 **institution_id** | **int**| Institution Id for Single site selection | [optional] 
 **name** | **str**| Name in minimum 1 character or routing number. | [optional] 
 **priority** | **str**| Search priority | [optional] 
 **provider_id** | **str**| Max 5 Comma seperated Provider Ids | [optional] 
 **skip** | **int**| skip (Min 0) - This is not applicable along with &#39;name&#39; parameter. | [optional] 
 **top** | **int**| top (Max 500) - This is not applicable along with &#39;name&#39; parameter. | [optional] 

### Return type

[**ProviderResponse**](ProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for priority&lt;br&gt;Y800 : Invalid value for providerName&lt;br&gt;Y801 : Invalid length for a site search. The search string must have atleast 1 character&lt;br&gt;Y800 : Invalid value for skip&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y821 : Dataset not supported&lt;br&gt;Y820 : The additionalDataSet is not supported for Get provider API |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> ProviderDetailResponse get_provider(provider_id)

Get Provider Details

The get provider detail service is used to get detailed information including the login form for a provider.<br>The response is a provider object that includes information such as name of the provider, <br>provider's base URL, a list of containers supported by the provider, the login form details of the provider, etc.<br>Only enabled datasets, attributes and containers gets returned in the response.<br><br><b>Note:</b><li>This service supports the localization feature and accepts locale as a header parameter.<li>The capability has been deprecated in the response.

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
    api_instance = yodlee.ProvidersApi(api_client)
    provider_id = 56 # int | providerId

    try:
        # Get Provider Details
        api_response = api_instance.get_provider(provider_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| providerId | 

### Return type

[**ProviderDetailResponse**](ProviderDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for providerId |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_count**
> ProvidersCountResponse get_providers_count(capability=capability, datasetfilter=datasetfilter, full_account_number_fields=full_account_number_fields, name=name, priority=priority)

Get Providers Count

The count service provides the total number of providers that get returned in the GET /providers depending on the input parameters passed.<br>If you are implementing pagination for providers, call this endpoint before calling GET /providers to know the number of providers that are returned for the input parameters passed.<br>The functionality of the input parameters remains the same as that of the GET /providers endpoint<br><br><b>Note:</b> <li>The capability has been deprecated in the query parameter.</li>

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
    api_instance = yodlee.ProvidersApi(api_client)
    capability = 'capability_example' # str | CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated (optional)
datasetfilter = 'datasetfilter_example' # str | Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. (optional)
full_account_number_fields = 'full_account_number_fields_example' # str | Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. (optional)
name = 'name_example' # str | Name in minimum 1 character or routing number. (optional)
priority = 'priority_example' # str | Search priority (optional)

    try:
        # Get Providers Count
        api_response = api_instance.get_providers_count(capability=capability, datasetfilter=datasetfilter, full_account_number_fields=full_account_number_fields, name=name, priority=priority)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProvidersApi->get_providers_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capability** | **str**| CHALLENGE_DEPOSIT_VERIFICATION - capability search is deprecated | [optional] 
 **datasetfilter** | **str**| Expression to filter the providers by dataset(s) or dataset attribute(s). The default value will be the dataset or dataset attributes configured as default for the customer. | [optional] 
 **full_account_number_fields** | **str**| Specify to filter the providers with values paymentAccountNumber,unmaskedAccountNumber. | [optional] 
 **name** | **str**| Name in minimum 1 character or routing number. | [optional] 
 **priority** | **str**| Search priority | [optional] 

### Return type

[**ProvidersCountResponse**](ProvidersCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for priority&lt;br&gt;Y800 : Invalid value for providerName&lt;br&gt;Y801 : Invalid length for a site search. The search string must have at least 1 character&lt;br&gt;Y800 : Invalid value for skip&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y821 : Dataset not supported&lt;br&gt;Y820 : The additionalDataSet is not supported for Get provider API |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

