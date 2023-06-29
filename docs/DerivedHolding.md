# DerivedHolding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The symbol of the security.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**exercised_quantity** | **float** | The quantity of the employee stock options that are already exercised or bought by the employee.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: Once the employee stock options is exercised, they are either converted to cash value or equity positions depending on the FI. The exercised quantity field is only applicable to employee stock options.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**cusip_number** | **str** | The CUSIP (Committee on Uniform Securities Identification Procedures) identifies most the financial instruments in the United States and Canada.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**asset_classification** | [**AssetClassification**](AssetClassification.md) |  | [optional] 
**vested_quantity** | **float** | The quantity of units or shares that are already vested on a vest date.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The vested quantity field is only applicable to employee stock options, restricted stock units/awards, performance units, etc.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**description** | **str** | The description (name) for the holding (E.g., Cisco Systems)&lt;br&gt;For insurance container, the field is only applicable for insurance annuity and variable life insurance types. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**unvested_value** | [**Money**](Money.md) |  | [optional] 
**security_style** | **str** | Indicates the security style of holding identified through the security service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**vested_value** | [**Money**](Money.md) |  | [optional] 
**option_type** | **str** | The type of the option position (i.e., put or call).&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The option type field is only applicable to options.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**last_updated** | **str** | The date when the information was last updated in the system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**match_status** | **str** | Indicates the security match status id of the investment option identified during security normalization.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**holding_type** | **str** | Type of holding&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**maturity_date** | **str** | The stated maturity date of a bond or CD.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**price** | [**Money**](Money.md) |  | [optional] 
**term** | **str** | The fixed duration for which the bond or CD is issued.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The term field is only applicable to CD.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**contract_quantity** | **float** | The quantity of tradeable units in a contract.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The contract quantity field is only applicable to commodity and currency.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**id** | **int** | Unique identifier for the security added in the system. This is the primary key of the holding resource.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**is_short** | **bool** | Indicates that the holding is a short trading.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**value** | [**Money**](Money.md) |  | [optional] 
**expiration_date** | **str** | The date on which an option, right or warrant expires.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The expiration date field is only applicable to options and employee stock options.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**interest_rate** | **float** | The interest rate on a CD.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The interest rate field is only applicable to CD.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**quantity** | **float** | The quantity held for the holding.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: Only for bonds the quantity field indicates the normalized quantity and not the quantity aggregated from the site. The quantity field is only applicable to restricted stock units/awards, performance units, currency, and commodity.&lt;br&gt;For insurance container, the field is only applicable for insurance annuity and variable life insurance types.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**accrued_interest** | [**Money**](Money.md) |  | [optional] 
**grant_date** | **str** | The date on which equity awards like ESOP, RSU, etc., are issued or granted.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The grant date field is only applicable to employee stock options, restricted stock units/awards, performance units, etc.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**sedol** | **str** | The SEDOL (Stock Exchange Daily Official List) is a set of security identifiers used in the United Kingdom and Ireland for clearing purposes.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The SEDOL field is only applicable to the trade related transactions&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**vested_shares_exercisable** | **float** | The number of vested shares that can be exercised by the employee. It is usually equal to the vested quantity.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The vested shares exercisable field is only applicable to employee stock options, restricted stock units/awards, performance units, etc.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**spread** | [**Money**](Money.md) |  | [optional] 
**account_id** | **int** | Unique identifier of the account to which the security is linked.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**enriched_description** | **str** | The enrichedDescription is the security description of the normalized holding&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**coupon_rate** | **float** | The stated interest rate for a bond.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**created_date** | **str** | The date on which the holding is created in the Yodlee system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**accrued_income** | [**Money**](Money.md) |  | [optional] 
**security_type** | **str** | Indicates the security type of holding identified through the security service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**provider_account_id** | **int** | Unique identifier for the user&#39;s association with the provider.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**unvested_quantity** | **float** | Indicates the number of unvested quantity or units.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The unvested quantity field is only applicable to employee stock options, restricted stock units/awards, performance units, etc.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**cost_basis** | [**Money**](Money.md) |  | [optional] 
**vesting_date** | **str** | The date on which a RSU, RSA, or an employee stock options become vested.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The vesting date field is only applicable to employee stock options, restricted stock units/awards, performance units, etc.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**isin** | **str** | The ISIN (International Securities Identification Number) is used worldwide to identify specific securities. It is equivalent to CUSIP for international markets.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The ISIN field is only applicable to the trade related transactions&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**strike_price** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


