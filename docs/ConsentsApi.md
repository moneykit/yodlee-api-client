# yodlee.ConsentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consent**](ConsentsApi.md#create_consent) | **POST** /consents | Post Consent
[**get_consent_details**](ConsentsApi.md#get_consent_details) | **GET** /consents/{consentId} | Get Authorization Details
[**get_consents**](ConsentsApi.md#get_consents) | **GET** /consents | Get Consents
[**renew_consent**](ConsentsApi.md#renew_consent) | **PUT** /consents/{consentId}/renewal | Renew Consent
[**update_consent**](ConsentsApi.md#update_consent) | **PUT** /consents/{consentId} | Put Consent


# **create_consent**
> CreatedConsentResponse create_consent(consent_request)

Post Consent

The generate consent service is used to generate all the consent information and permissions associated to a provider. <br/>The scope provided in the response is based on the providerId and the datasets provided in the input. <br/>If no dataset value is provided, the datasets that are configured for the customer will be considered. <br/>The configured dataset can be overridden by providing the dataset as an input. <br/>If no applicationName is provided in the input, the default applicationName will be considered. <b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

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
    api_instance = yodlee.ConsentsApi(api_client)
    consent_request = yodlee.CreateConsentRequest() # CreateConsentRequest | Unique identifier for the provider site(mandatory), the name of the application,  <br/>the flag responsible to include html content in the response, <br/>when passed as true and the name of the dataset attribute supported by the provider.

    try:
        # Post Consent
        api_response = api_instance.create_consent(consent_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsentsApi->create_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_request** | [**CreateConsentRequest**](CreateConsentRequest.md)| Unique identifier for the provider site(mandatory), the name of the application,  &lt;br/&gt;the flag responsible to include html content in the response, &lt;br/&gt;when passed as true and the name of the dataset attribute supported by the provider. | 

### Return type

[**CreatedConsentResponse**](CreatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for providerId &lt;br/&gt;Y807 : Resource not found &lt;br/&gt;Y800 : Invalid value for consentParam &lt;br/&gt;Y901 : Service not supported &lt;br/&gt;Y800 : Invalid value for applicationName &lt;br/&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consent_details**
> UpdatedConsentResponse get_consent_details(consent_id)

Get Authorization Details

The get authorization URL for consent service provides the authorization URL for the renew consent flow, within the consent dashboard.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

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
    api_instance = yodlee.ConsentsApi(api_client)
    consent_id = 56 # int | Consent Id generated through POST Consent.

    try:
        # Get Authorization Details
        api_response = api_instance.get_consent_details(consent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsentsApi->get_consent_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **int**| Consent Id generated through POST Consent. | 

### Return type

[**UpdatedConsentResponse**](UpdatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for consentId &lt;br/&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> ConsentResponse get_consents(consent_ids=consent_ids, include=include, provider_account_ids=provider_account_ids)

Get Consents

The get consent service is used to retrieve all the consents submitted to Yodlee. <br>The service can be used to build a manage consent interface or a consent dashboard to implement the renew and revoke consent flows.<br><b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

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
    api_instance = yodlee.ConsentsApi(api_client)
    consent_ids = 'consent_ids_example' # str | Consent Id generated through POST Consent. (optional)
include = 'include_example' # str | The flag responsible to include renew details like sharing duration and reauthorization required (optional)
provider_account_ids = 'provider_account_ids_example' # str | Unique identifier for the provider account resource. This is created during account addition. (optional)

    try:
        # Get Consents
        api_response = api_instance.get_consents(consent_ids=consent_ids, include=include, provider_account_ids=provider_account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsentsApi->get_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_ids** | **str**| Consent Id generated through POST Consent. | [optional] 
 **include** | **str**| The flag responsible to include renew details like sharing duration and reauthorization required | [optional] 
 **provider_account_ids** | **str**| Unique identifier for the provider account resource. This is created during account addition. | [optional] 

### Return type

[**ConsentResponse**](ConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_consent**
> RenewConsentResponse renew_consent(consent_id, renew_consent_request=renew_consent_request)

Renew Consent

The consent renewal service is used to renew the consent by validating the consent state. This API supports both UK and AU Open Banking. </br><b>Renewing an UK Open Banking consent:</b><br><li>Before the grace period of 90 days: The consent will be renewed using the third-party provider (TPP) renewal process that Yodlee does, and no consent reauthorisation is required.The API response will contain the complete renewed consent object.</li><li>After the grace period of 90 days: The API will provide an authorisation URL to redirect the user to the financial institution site to complete the consent reauthorization process.<br><b>Renewing an AU Open Banking consent:</b><br><li>Invoke this API, and in the API response, an authorisation URL will be provided to redirect the user to the financial institution site to complete the consent reauthorisation process.</li><br>

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
    api_instance = yodlee.ConsentsApi(api_client)
    consent_id = 56 # int | Consent Id to be renewed.
renew_consent_request = yodlee.RenewConsentRequest() # RenewConsentRequest | renewal entity from consent details service. (optional)

    try:
        # Renew Consent
        api_response = api_instance.renew_consent(consent_id, renew_consent_request=renew_consent_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsentsApi->renew_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **int**| Consent Id to be renewed. | 
 **renew_consent_request** | [**RenewConsentRequest**](RenewConsentRequest.md)| renewal entity from consent details service. | [optional] 

### Return type

[**RenewConsentResponse**](RenewConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for consentId &lt;br/&gt;Y800 : Invalid value for requestbody &lt;br/&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_consent**
> UpdatedConsentResponse update_consent(consent_id, consent_request)

Put Consent

The update consent service is used to capture the user acceptance of the consent presented to him or her. <br/>This service returns the authorization-redirect URL that should be used to display to the user, the bank's authentication interface.<b>Note:</b>This service supports the localization feature and accepts locale as a header parameter.<br>

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
    api_instance = yodlee.ConsentsApi(api_client)
    consent_id = 56 # int | Consent Id generated through POST Consent.
consent_request = yodlee.UpdateConsentRequest() # UpdateConsentRequest | Applicable Open Banking data cluster values.

    try:
        # Put Consent
        api_response = api_instance.update_consent(consent_id, consent_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsentsApi->update_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **int**| Consent Id generated through POST Consent. | 
 **consent_request** | [**UpdateConsentRequest**](UpdateConsentRequest.md)| Applicable Open Banking data cluster values. | 

### Return type

[**UpdatedConsentResponse**](UpdatedConsentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for consentId &lt;br/&gt;Y800 : Invalid value for consentParam &lt;br/&gt;Y812 : Required field/value - scopeId missing in the consentParam &lt;br/&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

