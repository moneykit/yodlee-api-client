# HistoricalBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | Date for which the account balance was provided.  This balance could be a carryforward, calculated or a scraped balance.&lt;br&gt;&lt;b&gt;Additional Details&lt;/b&gt;:&lt;br&gt;&lt;b&gt;Scraped&lt;/b&gt;: Balance shown in the provider site. This balance gets stored in Yodlee system during system/user account updates.&lt;br&gt;&lt;b&gt;CarryForward&lt;/b&gt;: Balance carried forward from the scraped balance to the days for which the balance was not available in the system. Balance may not be available for all the days in the system due to MFA information required, error in the site, credential changes, etc.&lt;br&gt;&lt;b&gt;calculated&lt;/b&gt;: Balances that gets calculated for the days that are prior to the account added date.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Both &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditCard, investment, insurance, realEstate, loan&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts/historicalBalances&lt;/li&gt;&lt;li&gt;GET derived/networth&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**is_asset** | **bool** | Indicates whether the balance is an asset or liability.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Both &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditCard, investment, insurance, realEstate, loan&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts/historicalBalances&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**balance** | [**Money**](Money.md) |  | [optional] 
**as_of_date** | **str** | Date as of when the balance is last updated due to the auto account updates or user triggered updates. This balance will be carry forward for the days where there is no balance available in the system. &lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Both &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditCard, investment, insurance, realEstate, loan&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts/historicalBalances&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**data_source_type** | **str** | The source of balance information.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Both &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank, creditCard, investment, insurance, realEstate, loan&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts/historicalBalances&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


