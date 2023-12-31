# yodlee.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_run_transaction_categorization_rules**](TransactionsApi.md#create_or_run_transaction_categorization_rules) | **POST** /transactions/categories/rules | Create or Run Transaction Categorization Rule
[**create_transaction_category**](TransactionsApi.md#create_transaction_category) | **POST** /transactions/categories | Create Category
[**delete_transaction_categorization_rule**](TransactionsApi.md#delete_transaction_categorization_rule) | **DELETE** /transactions/categories/rules/{ruleId} | Delete Transaction Categorization Rule
[**delete_transaction_category**](TransactionsApi.md#delete_transaction_category) | **DELETE** /transactions/categories/{categoryId} | Delete Category
[**get_transaction_categories**](TransactionsApi.md#get_transaction_categories) | **GET** /transactions/categories | Get Transaction Category List
[**get_transaction_categorization_rules**](TransactionsApi.md#get_transaction_categorization_rules) | **GET** /transactions/categories/txnRules | Get Transaction Categorization Rules
[**get_transaction_categorization_rules_deprecated**](TransactionsApi.md#get_transaction_categorization_rules_deprecated) | **GET** /transactions/categories/rules | Get Transaction Categorization Rules
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /transactions | Get Transactions
[**get_transactions_count**](TransactionsApi.md#get_transactions_count) | **GET** /transactions/count | Get Transactions Count
[**run_transaction_categorization_rule**](TransactionsApi.md#run_transaction_categorization_rule) | **POST** /transactions/categories/rules/{ruleId} | Run Transaction Categorization Rule
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /transactions/{transactionId} | Update Transaction
[**update_transaction_categorization_rule**](TransactionsApi.md#update_transaction_categorization_rule) | **PUT** /transactions/categories/rules/{ruleId} | Update Transaction Categorization Rule
[**update_transaction_category**](TransactionsApi.md#update_transaction_category) | **PUT** /transactions/categories | Update Category


# **create_or_run_transaction_categorization_rules**
> create_or_run_transaction_categorization_rules(action=action, rule_param=rule_param)

Create or Run Transaction Categorization Rule

The Create or Run Transaction Categorization Rule endpoint is used to: <br>Create transaction categorization rules for both system and user-defined categories.<br>Run all the transaction categorization rules to categorize transactions by calling the endpoint with action=run as the query parameter. <br><br>The input body parameters to create transaction categorization rules follow:<br>     categoryId - This field is mandatory and numeric<br>     priority - This field is optional and numeric. Priority decides the order in which the rule gets applied on transactions.<br>     ruleClause - This field is mandatory and should contain at least one rule<br>     field - The value can be description or amount<br><br>       If the field value is description then,<br>         1. operation - value can be stringEquals or stringContains<br>         2. value - value should be min of 3 and max of 50 characters<br><br>       If the field value is amount then, <br>         1. operation - value can be numberEquals, numberLessThan, numberLessThanEquals, numberGreaterThan or numberGreaterThanEquals<br>         2. value - min value 0 and a max value of 99999999999.99 is allowed<br>The HTTP response code is 201 (Created Successfully).

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
    api_instance = yodlee.TransactionsApi(api_client)
    action = 'action_example' # str | To run rules, pass action=run. Only value run is supported (optional)
rule_param = 'rule_param_example' # str | rules(JSON format) to categorize the transactions (optional)

    try:
        # Create or Run Transaction Categorization Rule
        api_instance.create_or_run_transaction_categorization_rules(action=action, rule_param=rule_param)
    except ApiException as e:
        print("Exception when calling TransactionsApi->create_or_run_transaction_categorization_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| To run rules, pass action&#x3D;run. Only value run is supported | [optional] 
 **rule_param** | **str**| rules(JSON format) to categorize the transactions | [optional] 

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
**201** | Created Successfully |  -  |
**400** | Y806 : Invalid input&lt;br&gt;Y400 : Rule already exists. Rule should be unique in terms of combination of description and amount |  -  |
**401** | Unauthorized |  -  |
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction_category**
> create_transaction_category(transaction_category_request)

Create Category

The create transaction categories service is used to create user-defined categories for a system-defined category.<br>The parentCategoryId is the system-defined category id.This can be retrieved using get transaction categories service.<br>The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.<br>The HTTP response code is 201 (Created successfully).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    transaction_category_request = yodlee.TransactionCategoryRequest() # TransactionCategoryRequest | User Transaction Category in JSON format

    try:
        # Create Category
        api_instance.create_transaction_category(transaction_category_request)
    except ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_category_request** | [**TransactionCategoryRequest**](TransactionCategoryRequest.md)| User Transaction Category in JSON format | 

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
**201** | Created Successfully |  -  |
**400** | Y800 : Invalid value for categoryParam&lt;br&gt;Y800 : Invalid value for source&lt;br&gt;Y801 : Invalid length for categoryName. Min 1 and max 50 is required&lt;br&gt;Y803 : parentCategoryId required&lt;br&gt;Y811 : categoryName value already exists |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_categorization_rule**
> delete_transaction_categorization_rule(rule_id)

Delete Transaction Categorization Rule

The delete transaction categorization rule service is used to delete the given user-defined transaction categorization rule for both system-defined category as well as user-defined category.<br>This will delete all the corresponding rule clauses associated with the rule.<br>The HTTP response code is 204 (Success without content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    rule_id = 56 # int | ruleId

    try:
        # Delete Transaction Categorization Rule
        api_instance.delete_transaction_categorization_rule(rule_id)
    except ApiException as e:
        print("Exception when calling TransactionsApi->delete_transaction_categorization_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| ruleId | 

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
**400** | Y800 : Invalid value for ruleId |  -  |
**401** | Unauthorized |  -  |
**204** | Deleted Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_category**
> delete_transaction_category(category_id)

Delete Category

The delete transaction categories service is used to delete the given user-defined category.<br>The HTTP response code is 204 (Success without content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    category_id = 56 # int | categoryId

    try:
        # Delete Category
        api_instance.delete_transaction_category(category_id)
    except ApiException as e:
        print("Exception when calling TransactionsApi->delete_transaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| categoryId | 

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
**400** | Y800 : Invalid value for categoryId |  -  |
**401** | Unauthorized |  -  |
**204** | Deleted Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_categories**
> TransactionCategoryResponse get_transaction_categories()

Get Transaction Category List

The categories service returns the list of available transaction categories.<br>High level category is returned in the response only if it is opted by the customer.<br>When invoked by passing the cobrand session or admin access token, this service returns the supported transaction categories at the cobrand level. <br>When invoked by passing the cobrand session and the user session or user access token, this service returns the transaction categories <br>along with user-defined categories.<br>Double quotes in the user-defined category name will be prefixed by backslashes (&#92;) in the response, <br>e.g. Toys \"R\" Us.<br/>Source and id are the primary attributes of the category entity.<br><br><b>Note:</b><li>This service supports the localization feature and accepts locale as a header parameter.</li>

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
    api_instance = yodlee.TransactionsApi(api_client)
    
    try:
        # Get Transaction Category List
        api_response = api_instance.get_transaction_categories()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionCategoryResponse**](TransactionCategoryResponse.md)

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

# **get_transaction_categorization_rules**
> TransactionCategorizationRuleResponse get_transaction_categorization_rules()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    
    try:
        # Get Transaction Categorization Rules
        api_response = api_instance.get_transaction_categorization_rules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_categorization_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionCategorizationRuleResponse**](TransactionCategorizationRuleResponse.md)

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

# **get_transaction_categorization_rules_deprecated**
> list[TransactionCategorizationRule] get_transaction_categorization_rules_deprecated()

Get Transaction Categorization Rules

The get transaction categorization rule service is used to get all the categorization rules.<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    
    try:
        # Get Transaction Categorization Rules
        api_response = api_instance.get_transaction_categorization_rules_deprecated()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_categorization_rules_deprecated: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TransactionCategorizationRule]**](TransactionCategorizationRule.md)

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

# **get_transactions**
> TransactionResponse get_transactions(account_id=account_id, base_type=base_type, category_id=category_id, category_type=category_type, container=container, detail_category_id=detail_category_id, from_date=from_date, high_level_category_id=high_level_category_id, keyword=keyword, skip=skip, to_date=to_date, top=top, type=type)

Get Transactions

The Transaction service is used to get a list of transactions for a user.<br>By default, this service returns the last 30 days of transactions from today's date.<br>The keyword parameter performs a contains search on the original, consumer, and simple description attributes, replace the special characters #, &, and + with percent-encoding values %23, %26, and %2B respectively. Eg: for -Debit# , pass the input as -Debit%23.<br>Values for categoryId parameter can be fetched from get transaction category list service.<br> The categoryId is used to filter transactions based on system-defined category as well as user-defined category.<br>User-defined categoryIds should be provided in the filter with the prefix ''U''. E.g. U10002<br>The skip and top parameters are used for pagination. In the skip and top parameters pass the number of records to be skipped and retrieved, respectively. The response header provides the links to retrieve the next and previous set of transactions.<br>Double quotes in the merchant name will be prefixed by backslashes (&#92;) in the response, e.g. Toys \"R\" Us. <br>sourceId is a unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts. Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.<br><br><b>Note</b><ul><li><a href=\"https://developer.yodlee.com/docs/api/1.1/Transaction_Data_Enrichment\">TDE</a> is made available for bank and card accounts. The address field in the response is available only when the TDE key is turned on.</li><li>The pagination feature is available by default. If no values are passed in the skip and top parameters, the API will only return the first 500 transactions.</li><li>This service supports the localization feature and accepts locale as a header parameter.</li></ul>

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
    api_instance = yodlee.TransactionsApi(api_client)
    account_id = 'account_id_example' # str | Comma separated accountIds (optional)
base_type = 'base_type_example' # str | DEBIT/CREDIT (optional)
category_id = 'category_id_example' # str | Comma separated categoryIds (optional)
category_type = 'category_type_example' # str | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) (optional)
container = 'container_example' # str | bank/creditCard/investment/insurance/loan (optional)
detail_category_id = 'detail_category_id_example' # str | Comma separated detailCategoryIds (optional)
from_date = 'from_date_example' # str | Transaction from date(YYYY-MM-DD) (optional)
high_level_category_id = 'high_level_category_id_example' # str | Comma separated highLevelCategoryIds (optional)
keyword = 'keyword_example' # str | Transaction search text (optional)
skip = 56 # int | skip (Min 0) (optional)
to_date = 'to_date_example' # str | Transaction end date (YYYY-MM-DD) (optional)
top = 56 # int | top (Max 500) (optional)
type = 'type_example' # str | Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment (optional)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions(account_id=account_id, base_type=base_type, category_id=category_id, category_type=category_type, container=container, detail_category_id=detail_category_id, from_date=from_date, high_level_category_id=high_level_category_id, keyword=keyword, skip=skip, to_date=to_date, top=top, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountIds | [optional] 
 **base_type** | **str**| DEBIT/CREDIT | [optional] 
 **category_id** | **str**| Comma separated categoryIds | [optional] 
 **category_type** | **str**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] 
 **container** | **str**| bank/creditCard/investment/insurance/loan | [optional] 
 **detail_category_id** | **str**| Comma separated detailCategoryIds | [optional] 
 **from_date** | **str**| Transaction from date(YYYY-MM-DD) | [optional] 
 **high_level_category_id** | **str**| Comma separated highLevelCategoryIds | [optional] 
 **keyword** | **str**| Transaction search text | [optional] 
 **skip** | **int**| skip (Min 0) | [optional] 
 **to_date** | **str**| Transaction end date (YYYY-MM-DD) | [optional] 
 **top** | **int**| top (Max 500) | [optional] 
 **type** | **str**| Transaction Type(SELL,SWEEP, etc.) for bank/creditCard/investment | [optional] 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for baseType&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for category&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y800 : Invalid value for container&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y804 : Permitted values of top between 1 - 500&lt;br&gt;Y805 : Multiple containers not supported&lt;br&gt;Y800 : Invalid value for transaction type&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100&lt;br&gt;Y824 : The maximum number of categoryIds permitted is 100&lt;br&gt;Y824 : The maximum number of highLevelCategoryIds permitted is 100&lt;br&gt;Y848 : detailCategoryId cannot be provided as input, as the detailedCategory feature is not enabled&lt;br&gt;Y823 : detailCategoryId is not for applicable containers other than bank and card&lt;br&gt;Y824 : The maximum number of detailCategoryIds permitted is 100&lt;br&gt;Y800 : Invalid value for detailCategoryId |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_count**
> TransactionCountResponse get_transactions_count(account_id=account_id, base_type=base_type, category_id=category_id, category_type=category_type, container=container, detail_category_id=detail_category_id, from_date=from_date, high_level_category_id=high_level_category_id, keyword=keyword, to_date=to_date, type=type)

Get Transactions Count

The count service provides the total number of transactions for a specific user depending on the input parameters passed.<br>If you are implementing pagination for transactions, call this endpoint before calling GET /transactions to know the number of transactions that are returned for the input parameters passed.<br>The functionality of the input parameters remains the same as that of the GET /transactions endpoint.<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    account_id = 'account_id_example' # str | Comma separated accountIds  (optional)
base_type = 'base_type_example' # str | DEBIT/CREDIT (optional)
category_id = 'category_id_example' # str | Comma separated categoryIds (optional)
category_type = 'category_type_example' # str | Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) (optional)
container = 'container_example' # str | bank/creditCard/investment/insurance/loan (optional)
detail_category_id = 'detail_category_id_example' # str | Comma separated detailCategoryIds (optional)
from_date = 'from_date_example' # str | Transaction from date(YYYY-MM-DD) (optional)
high_level_category_id = 'high_level_category_id_example' # str | Comma separated highLevelCategoryIds (optional)
keyword = 'keyword_example' # str | Transaction search text  (optional)
to_date = 'to_date_example' # str | Transaction end date (YYYY-MM-DD) (optional)
type = 'type_example' # str | Transaction Type(SELL,SWEEP, etc.) (optional)

    try:
        # Get Transactions Count
        api_response = api_instance.get_transactions_count(account_id=account_id, base_type=base_type, category_id=category_id, category_type=category_type, container=container, detail_category_id=detail_category_id, from_date=from_date, high_level_category_id=high_level_category_id, keyword=keyword, to_date=to_date, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountIds  | [optional] 
 **base_type** | **str**| DEBIT/CREDIT | [optional] 
 **category_id** | **str**| Comma separated categoryIds | [optional] 
 **category_type** | **str**| Transaction Category Type(UNCATEGORIZE, INCOME, TRANSFER, EXPENSE or DEFERRED_COMPENSATION) | [optional] 
 **container** | **str**| bank/creditCard/investment/insurance/loan | [optional] 
 **detail_category_id** | **str**| Comma separated detailCategoryIds | [optional] 
 **from_date** | **str**| Transaction from date(YYYY-MM-DD) | [optional] 
 **high_level_category_id** | **str**| Comma separated highLevelCategoryIds | [optional] 
 **keyword** | **str**| Transaction search text  | [optional] 
 **to_date** | **str**| Transaction end date (YYYY-MM-DD) | [optional] 
 **type** | **str**| Transaction Type(SELL,SWEEP, etc.) | [optional] 

### Return type

[**TransactionCountResponse**](TransactionCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Y800 : Invalid value for detailCategoryId&lt;br&gt;Y848 : detailCategoryId cannot be provided as input, as the detailedCategory feature is not enabled&lt;br&gt;Y823 : detailCategoryId is not applicable for containers other than bank and card&lt;br&gt;Y824 : The maximum number of detailCategoryIds permitted is 100&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_transaction_categorization_rule**
> run_transaction_categorization_rule(action, rule_id)

Run Transaction Categorization Rule

The run transaction categorization rule service is used to run a rule on transactions, to categorize the transactions.<br>The HTTP response code is 204 (Success with no content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    action = 'run' # str |  (default to 'run')
rule_id = 56 # int | Unique id of the categorization rule

    try:
        # Run Transaction Categorization Rule
        api_instance.run_transaction_categorization_rule(action, rule_id)
    except ApiException as e:
        print("Exception when calling TransactionsApi->run_transaction_categorization_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [default to &#39;run&#39;]
 **rule_id** | **int**| Unique id of the categorization rule | 

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
**400** | Y800 : Invalid value for ruleId&lt;br&gt;Y400 : Categorization already in progress |  -  |
**401** | Unauthorized |  -  |
**204** | Run Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> update_transaction(transaction_id, transaction_request)

Update Transaction

The update transaction service is used to update the category,consumer description, memo, isPhysical, merchantType, detailCategory for a transaction.<br>The HTTP response code is 204 (Success without content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    transaction_id = 56 # int | transactionId
transaction_request = yodlee.TransactionRequest() # TransactionRequest | transactionRequest

    try:
        # Update Transaction
        api_instance.update_transaction(transaction_id, transaction_request)
    except ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| transactionId | 
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)| transactionRequest | 

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
**400** | Y812 : Required field -container missing in the transactionParam parameter input&lt;br&gt;Y800 : Invalid value for transactionId&lt;br&gt;Y800 : Invalid value for merchantType&lt;br&gt;Y800 : Invalid value for detailCategoryId&lt;br&gt;Y800 : Invalid value for categoryId&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
**401** | Unauthorized |  -  |
**204** | Updated Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_categorization_rule**
> update_transaction_categorization_rule(rule_id, transaction_categories_rule_request)

Update Transaction Categorization Rule

The update transaction categorization rule service is used to update a categorization rule for both system-defined category as well as user-defined category.<br>ruleParam JSON input should be as explained in the create transaction categorization rule service.<br>The HTTP response code is 204 (Success without content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    rule_id = 56 # int | ruleId
transaction_categories_rule_request = yodlee.TransactionCategorizationRuleRequest() # TransactionCategorizationRuleRequest | transactionCategoriesRuleRequest

    try:
        # Update Transaction Categorization Rule
        api_instance.update_transaction_categorization_rule(rule_id, transaction_categories_rule_request)
    except ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction_categorization_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| ruleId | 
 **transaction_categories_rule_request** | [**TransactionCategorizationRuleRequest**](TransactionCategorizationRuleRequest.md)| transactionCategoriesRuleRequest | 

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
**400** | Y800 : Invalid value for ruleId&lt;br&gt;Y806 : Invalid input |  -  |
**401** | Unauthorized |  -  |
**204** | Updated Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_category**
> update_transaction_category(update_category_request)

Update Category

The update transaction categories service is used to update the transaction category name<br>for a high level category, a system-defined category and a user-defined category.<br>The renamed category can be set back to the original name by passing an empty string for categoryName.<br>The categoryName can accept minimum of 1, maximum of 50 alphanumeric or special characters.<br>The HTTP response code is 204 (Success without content).<br>

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
    api_instance = yodlee.TransactionsApi(api_client)
    update_category_request = yodlee.UpdateCategoryRequest() # UpdateCategoryRequest | updateCategoryRequest

    try:
        # Update Category
        api_instance.update_transaction_category(update_category_request)
    except ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_category_request** | [**UpdateCategoryRequest**](UpdateCategoryRequest.md)| updateCategoryRequest | 

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
**400** | Y800 : Invalid value for categoryParam&lt;br&gt;Y800 : Invalid value for source&lt;br&gt;Y801 : Invalid length for categoryName. Min 1 and max 50 is required&lt;br&gt;Y803 : id required&lt;br&gt;Y811 : categoryName value already exists |  -  |
**401** | Unauthorized |  -  |
**204** | Updated Successfully |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

