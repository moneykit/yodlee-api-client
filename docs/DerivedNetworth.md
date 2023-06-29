# DerivedNetworth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | The date as of when the networth information is provided.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] [readonly] 
**liability** | [**Money**](Money.md) |  | [optional] 
**historical_balances** | [**list[DerivedNetworthHistoricalBalance]**](DerivedNetworthHistoricalBalance.md) | Balances of the accounts over the period of time.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditcard, investment, insurance, realEstate, loan&lt;br&gt; | [optional] [readonly] 
**networth** | [**Money**](Money.md) |  | [optional] 
**asset** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


