# DerivedCategorySummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_total** | [**Money**](Money.md) |  | [optional] 
**details** | [**list[DerivedCategorySummaryDetails]**](DerivedCategorySummaryDetails.md) | Credit and debit summary per date.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] [readonly] 
**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) |  | [optional] 
**category_name** | **str** | The name of the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] [readonly] 
**category_id** | **int** | Id of the category. This information is provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] [readonly] 
**debit_total** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


