# yodlee.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key**](AuthApi.md#delete_api_key) | **DELETE** /auth/apiKey/{key} | Delete API Key
[**delete_token**](AuthApi.md#delete_token) | **DELETE** /auth/token | Delete Token
[**generate_access_token**](AuthApi.md#generate_access_token) | **POST** /auth/token | Generate Access Token
[**generate_api_key**](AuthApi.md#generate_api_key) | **POST** /auth/apiKey | Generate API Key
[**get_api_keys**](AuthApi.md#get_api_keys) | **GET** /auth/apiKey | Get API Keys


# **delete_api_key**
> delete_api_key(key)

Delete API Key

This endpoint allows an existing API key to be deleted.<br>You can use one of the following authorization methods to access this API:<br><ol><li>cobsession</li><li>JWT token</li></ol> <b>Notes:</b> <li>This service is not available in developer sandbox environment and will be made availablefor testing in your dedicated environment. 

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
    api_instance = yodlee.AuthApi(api_client)
    key = 'key_example' # str | key

    try:
        # Delete API Key
        api_instance.delete_api_key(key)
    except ApiException as e:
        print("Exception when calling AuthApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 

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
**201** | OK |  -  |
**400** | Y807 : Resource not found&lt;br&gt;Y806 : Invalid input |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token()

Delete Token

This endpoint revokes the token passed in the Authorization header. This service is applicable for JWT-based (and all API key-based) authentication and also client credential (clientId and secret) based authentication. This service does not return a response body. The HTTP response code is 204 (success with no content). <br>Tokens generally have limited lifetime of up to 30 minutes. You will call this service when you finish working with one user, and you want to delete the valid token rather than simply letting it expire.<br><br><b>Note:</b> <li>Revoking an access token (either type, admin or a user token) can take up to 2 minutes, as the tokens are stored on a distributed system.<br/>

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
    api_instance = yodlee.AuthApi(api_client)
    
    try:
        # Delete Token
        api_instance.delete_token()
    except ApiException as e:
        print("Exception when calling AuthApi->delete_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**401** | Y020 : Invalid token in authorization header&lt;br&gt;Y023 : Token has expired&lt;br&gt;Y016 : Api-Version header missing&lt;br&gt;Y015 : Unauthorized User&lt;br&gt;Y027 : Unsupported authentication type&lt;br&gt;Y007 : Authorization header missing&lt;br&gt;Y020 : Invalid token in authorization header |  -  |
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_access_token**
> ClientCredentialTokenResponse generate_access_token(client_id=client_id, secret=secret)

Generate Access Token

<b>Generate Access Token using client credential authentication.</b><br>This service returns access tokens required to access Yodlee 1.1 APIs. These tokens are the simplest and easiest of several alternatives for authenticating with Yodlee servers.<br>The most commonly used services obtain data specific to an end user (your customer). For these services, you need a <b>user access token</b>. These are simply tokens created with the user name parameter (<b>loginName</b>) set to the id of your end user.  <i><br><br><b>Note:</b> You determine this id and you must ensure it's unique among all your customers.</i> <br><br>Each token issued has an associated user. The token passed in the http headers explicitly names the user referenced in that API call.<br><br>Some of the APIs do administrative work, and don't reference an end user. <br/>One example of administrative work is key management. Another example is registering a new user explicitly, with <b>POST /user/register</b> call or subscribe to webhook, with <b>POST /config/notifications/events/{eventName}</b>. <br/>To invoke these, you need an <b>admin access token</b>. Create this by passing in your admin user login name in place of a regular user name.<br><br>This service also allows for simplified registration of new users. Any time you pass in a user name not already in use, the system will automatically implicitly create a new user for you. <br>This user will naturally have very few associated details. You can later provide additional user information by calling the <b>PUT user/register service</b>.<br><br><b>Notes:</b><ul><li>The header <code>Authorization</code> does not apply to this service.</li><li>The content type has to be passed as application/x-www-form-urlencoded.<li>Upgrading to client credential authentication requires infrastructure reconfiguration. <li>Customers wishing to switch from another authentication scheme to client credential authentication, please contact Yodlee Client Services.</li><li>Default expiry time of user access token and admin access token is 30 minutes.</li></ul>

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
    api_instance = yodlee.AuthApi(api_client)
    client_id = 'client_id_example' # str | clientId issued by Yodlee is used to generate the OAuth token for authentication. (optional)
secret = 'secret_example' # str | secret issued by Yodlee is used to generate the OAuth token for authentication. (optional)

    try:
        # Generate Access Token
        api_response = api_instance.generate_access_token(client_id=client_id, secret=secret)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->generate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| clientId issued by Yodlee is used to generate the OAuth token for authentication. | [optional] 
 **secret** | **str**| secret issued by Yodlee is used to generate the OAuth token for authentication. | [optional] 

### Return type

[**ClientCredentialTokenResponse**](ClientCredentialTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Y800 : Invalid value for loginName&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y801 : Invalid length for loginName&lt;br&gt;Y303 : clientId or secret is missing&lt;br&gt;Y301 : Invalid clientId or secret&lt;br&gt;Y305 : Access token can be issued only for pre-registered users&lt;br&gt;Y004 : Inactive user&lt;br&gt;Y901 : Service not supported&lt;br&gt; |  -  |
**401** | Y016 : loginName header missing&lt;br&gt;Y015 : Unauthorized User&lt;br&gt;Y016 : Api-Version header missing&lt;br&gt;Y020 : Invalid token in authorization header&lt;br&gt;Y027 : Unsupported authentication type |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> ApiKeyResponse generate_api_key(api_key_request)

Generate API Key

This endpoint is used to generate an API key. The RSA public key you provide should be in 2048 bit PKCS#8 encoded format. <br>A public key is a mandatory input for generating the API key.<br/>The public key should be a unique key. The apiKeyId you get in the response is what you should use to generate the JWT token.<br> You can use one of the following authorization methods to access<br/>this API:<br><ol><li>cobsession</li><li>JWT token</li></ol> Alternatively, you can use base 64 encoded cobrandLogin and cobrandPassword in the Authorization header (Format: Authorization: Basic <encoded value of cobrandLogin: cobrandPassword>)<br><br><b>Note:</b><br><li>This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. The content type has to be passed as application/json for the body parameter.</li>

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
    api_instance = yodlee.AuthApi(api_client)
    api_key_request = yodlee.ApiKeyRequest() # ApiKeyRequest | apiKeyRequest

    try:
        # Generate API Key
        api_response = api_instance.generate_api_key(api_key_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**ApiKeyRequest**](ApiKeyRequest.md)| apiKeyRequest | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Y800 : Invalid value for RS512 publicKey&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y824 : The maximum number of apiKey permitted is 5&lt;br&gt;Y811 : publicKey value already exists |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> ApiKeyResponse get_api_keys()

Get API Keys

This endpoint provides the list of API keys that exist for a customer.<br>You can use one of the following authorization methods to access this API:<br><ol><li>cobsession</li><li>JWT token</li></ol><b>Notes:</b><li>This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. 

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
    api_instance = yodlee.AuthApi(api_client)
    
    try:
        # Get API Keys
        api_response = api_instance.get_api_keys()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->get_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

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

