# DerivedTransactionsSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_type** | **str** | Type of categories provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**category_summary** | [**list[DerivedCategorySummary]**](DerivedCategorySummary.md) | Summary of transaction amouts at category level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; | [optional] [readonly] 
**credit_total** | [**Money**](Money.md) |  | [optional] 
**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) |  | [optional] 
**debit_total** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


