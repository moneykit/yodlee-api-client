# yodlee.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{documentId} | Delete Document
[**download_document**](DocumentsApi.md#download_document) | **GET** /documents/{documentId} | Download a Document
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /documents | Get Documents


# **delete_document**
> delete_document(document_id)

Delete Document

The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).<br>Documents can be deleted only if the document related dataset attributes are subscribed.<br>

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
    api_instance = yodlee.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | documentId

    try:
        # Delete Document
        api_instance.delete_document(document_id)
    except ApiException as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| documentId | 

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
**400** | Y800 : Invalid value for documentId&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**204** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> DocumentDownloadResponse download_document(document_id)

Download a Document

The get document details service allows consumers to download a document. The document is provided in base64.<br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>

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
    api_instance = yodlee.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | documentId

    try:
        # Download a Document
        api_response = api_instance.download_document(document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| documentId | 

### Return type

[**DocumentDownloadResponse**](DocumentDownloadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for documentId |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> DocumentResponse get_documents(keyword=keyword, account_id=account_id, doc_type=doc_type, from_date=from_date, to_date=to_date)

Get Documents

The get documents service allows customers to search or retrieve metadata related to documents. <br>The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. <br>This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. <br>

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
    api_instance = yodlee.DocumentsApi(api_client)
    keyword = 'keyword_example' # str | The string used to search a document by its name. (optional)
account_id = 'account_id_example' # str | The unique identifier of an account. Retrieve documents for a given accountId. (optional)
doc_type = 'doc_type_example' # str | Accepts only one of the following valid document types: STMT, TAX, and EBILL. (optional)
from_date = 'from_date_example' # str | The date from which documents have to be retrieved. (optional)
to_date = 'to_date_example' # str | The date to which documents have to be retrieved. (optional)

    try:
        # Get Documents
        api_response = api_instance.get_documents(keyword=keyword, account_id=account_id, doc_type=doc_type, from_date=from_date, to_date=to_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| The string used to search a document by its name. | [optional] 
 **account_id** | **str**| The unique identifier of an account. Retrieve documents for a given accountId. | [optional] 
 **doc_type** | **str**| Accepts only one of the following valid document types: STMT, TAX, and EBILL. | [optional] 
 **from_date** | **str**| The date from which documents have to be retrieved. | [optional] 
 **to_date** | **str**| The date to which documents have to be retrieved. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y800 : Invalid value for docType |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

