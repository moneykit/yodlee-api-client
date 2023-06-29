# yodlee.ConfigsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_notification_event**](ConfigsApi.md#create_subscription_notification_event) | **POST** /configs/notifications/events/{eventName} | Subscribe For Notification Event
[**delete_subscribed_notification_event**](ConfigsApi.md#delete_subscribed_notification_event) | **DELETE** /configs/notifications/events/{eventName} | Delete Notification Subscription
[**get_public_encryption_key**](ConfigsApi.md#get_public_encryption_key) | **GET** /configs/publicKey | Get Public Key
[**get_subscribed_notification_events**](ConfigsApi.md#get_subscribed_notification_events) | **GET** /configs/notifications/events | Get Subscribed Notification Events
[**update_subscribed_notification_event**](ConfigsApi.md#update_subscribed_notification_event) | **PUT** /configs/notifications/events/{eventName} | Update Notification Subscription


# **create_subscription_notification_event**
> create_subscription_notification_event(event_name, event_request)

Subscribe For Notification Event

The subscribe events service is used to subscribe to an event for receiving notifications.<br>The callback URL, where the notification will be posted should be provided to this service.<br>If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.<br>Customers can subscribe to REFRESH,DATA_UPDATES,AUTO_REFRESH_UPDATE and LATEST_BALANCE_UPDATES.<br><br><b>Notes:</b><li>This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.<li>The content type has to be passed as application/json for the body parameter.</li>

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
    api_instance = yodlee.ConfigsApi(api_client)
    event_name = 'event_name_example' # str | eventName
event_request = yodlee.CreateConfigsNotificationEventRequest() # CreateConfigsNotificationEventRequest | eventRequest

    try:
        # Subscribe For Notification Event
        api_instance.create_subscription_notification_event(event_name, event_request)
    except ApiException as e:
        print("Exception when calling ConfigsApi->create_subscription_notification_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 
 **event_request** | [**CreateConfigsNotificationEventRequest**](CreateConfigsNotificationEventRequest.md)| eventRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Y803 : eventName required&lt;br&gt;Y803 : callbackUrl required&lt;br&gt;Y800 : Invalid value for callbackUrl&lt;br&gt;Y901 : Service not supported&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscribed_notification_event**
> delete_subscribed_notification_event(event_name)

Delete Notification Subscription

The delete events service is used to unsubscribe from an events service.<br>

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
    api_instance = yodlee.ConfigsApi(api_client)
    event_name = 'event_name_example' # str | eventName

    try:
        # Delete Notification Subscription
        api_instance.delete_subscribed_notification_event(event_name)
    except ApiException as e:
        print("Exception when calling ConfigsApi->delete_subscribed_notification_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 

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
**400** | Y803 : eventName required |  -  |
**401** | Unauthorized |  -  |
**204** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_encryption_key**
> ConfigsPublicKeyResponse get_public_encryption_key()

Get Public Key

The get public key service provides the public key that should be used to encrypt user credentials while invoking POST /providerAccounts and PUT /providerAccounts endpoints.<br>This service will only work if the PKI (public key infrastructure) feature is enabled for the customer.<br><br><b>Note:</b><li> The key in the response is a string in PEM format.</li><li>This endpoint is not available in the Sandbox environment and it is useful only if the PKI feature is enabled.</li>

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
    api_instance = yodlee.ConfigsApi(api_client)
    
    try:
        # Get Public Key
        api_response = api_instance.get_public_encryption_key()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigsApi->get_public_encryption_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigsPublicKeyResponse**](ConfigsPublicKeyResponse.md)

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

# **get_subscribed_notification_events**
> ConfigsNotificationResponse get_subscribed_notification_events(event_name=event_name)

Get Subscribed Notification Events

The get events service provides the list of events for which consumers subscribed to receive notifications. <br>

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
    api_instance = yodlee.ConfigsApi(api_client)
    event_name = 'event_name_example' # str | eventName (optional)

    try:
        # Get Subscribed Notification Events
        api_response = api_instance.get_subscribed_notification_events(event_name=event_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigsApi->get_subscribed_notification_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | [optional] 

### Return type

[**ConfigsNotificationResponse**](ConfigsNotificationResponse.md)

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

# **update_subscribed_notification_event**
> update_subscribed_notification_event(event_name, event_request)

Update Notification Subscription

The update events service is used to update the callback URL.<br>If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.<br><br><b>Note:</b> <li>The content type has to be passed as application/json for the body parameter. <br>

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
    api_instance = yodlee.ConfigsApi(api_client)
    event_name = 'event_name_example' # str | eventName
event_request = yodlee.UpdateConfigsNotificationEventRequest() # UpdateConfigsNotificationEventRequest | eventRequest

    try:
        # Update Notification Subscription
        api_instance.update_subscribed_notification_event(event_name, event_request)
    except ApiException as e:
        print("Exception when calling ConfigsApi->update_subscribed_notification_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| eventName | 
 **event_request** | [**UpdateConfigsNotificationEventRequest**](UpdateConfigsNotificationEventRequest.md)| eventRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Y803 : eventName required&lt;br&gt;Y803 : callbackUrl required&lt;br&gt;Y800 : Invalid value for callbackUrl |  -  |
**401** | Unauthorized |  -  |
**204** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

